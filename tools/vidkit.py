#!/usr/bin/env python3
"""vidkit - make fal/Kling videos web-ready for looping <video> backgrounds.

Uses the ffmpeg binary bundled by the `imageio-ffmpeg` pip package (no system
ffmpeg needed).

Commands
--------
web    IN OUT [--max 1280] [--crf 30] [--fps 24]
    Scale to <= --max wide, strip audio, H.264 + faststart (web hero loops).
    Typically turns a 20 MB Kling clip into ~1.5-4 MB.

webm   IN OUT [--max 1280] [--crf 34]
    Same but VP9/webm (smaller; pair as a <source> before the mp4).

poster IN OUT [--time 0]
    Extract a frame as a JPEG poster / fallback image for the <video>.

loop   IN OUT [--xfade 0.5]
    Make a seamless loop by cross-fading the tail back over the head.

pingpong IN OUT [--crf 30]
    Forward-then-reversed "boomerang" loop: the clip plays out and rewinds so
    start/end frames always match — no hard cut at the seam. Smoothest idle for
    a muted autoplay <video>. Doubles the duration (5s clip -> ~10s loop).

Examples
--------
    python3 tools/vidkit.py web    raw/hero.mp4 assets/video/hero.mp4 --max 1280
    python3 tools/vidkit.py poster raw/hero.mp4 assets/video/hero-poster.jpg
"""
import argparse
import subprocess
import sys

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def run(args):
    print("  ffmpeg", " ".join(args[1:]))
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != 0:
        sys.exit("ffmpeg failed:\n" + p.stderr[-1500:])


def cmd_web(a):
    vf = f"scale='min({a.max},iw)':-2:flags=lanczos,fps={a.fps}"
    run([FF, "-y", "-i", a.IN, "-an", "-vf", vf, "-c:v", "libx264",
         "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", str(a.crf),
         "-preset", "slow", "-movflags", "+faststart", a.OUT])
    print(f"web -> {a.OUT}")


def cmd_webm(a):
    vf = f"scale='min({a.max},iw)':-2:flags=lanczos"
    run([FF, "-y", "-i", a.IN, "-an", "-vf", vf, "-c:v", "libvpx-vp9",
         "-b:v", "0", "-crf", str(a.crf), "-row-mt", "1", a.OUT])
    print(f"webm -> {a.OUT}")


def cmd_poster(a):
    run([FF, "-y", "-ss", str(a.time), "-i", a.IN, "-frames:v", "1",
         "-q:v", "3", a.OUT])
    print(f"poster -> {a.OUT}")


def cmd_loop(a):
    # crossfade the tail back over the head for a seamless restart
    flt = (f"[0:v]split[a][b];[a]trim=start={a.xfade},setpts=PTS-STARTPTS[main];"
           f"[b]trim=duration={a.xfade},setpts=PTS-STARTPTS[head];"
           f"[main][head]xfade=transition=fade:duration={a.xfade}:offset=0,format=yuv420p[v]")
    run([FF, "-y", "-i", a.IN, "-filter_complex", flt, "-map", "[v]",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "30",
         "-movflags", "+faststart", a.OUT])
    print(f"loop -> {a.OUT}")


def cmd_pingpong(a):
    # Forward then reversed = a "boomerang" loop. The clip plays out and
    # rewinds, so the start/end frames always match and there is NO hard cut
    # at the loop seam — smoothest possible idle for a muted autoplay <video>.
    # Drop the duplicated turnaround/seam frames so motion doesn't stutter.
    flt = ("[0:v]split[f][r];"
           "[r]reverse,trim=start_frame=1,setpts=PTS-STARTPTS[rev];"
           "[f][rev]concat=n=2:v=1:a=0,format=yuv420p[v]")
    run([FF, "-y", "-i", a.IN, "-filter_complex", flt, "-map", "[v]", "-an",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-crf", str(a.crf), "-preset", "slow", "-movflags", "+faststart", a.OUT])
    print(f"pingpong -> {a.OUT}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)

    w = s.add_parser("web"); w.add_argument("IN"); w.add_argument("OUT")
    w.add_argument("--max", type=int, default=1280); w.add_argument("--crf", type=int, default=30)
    w.add_argument("--fps", type=int, default=24); w.set_defaults(func=cmd_web)

    wm = s.add_parser("webm"); wm.add_argument("IN"); wm.add_argument("OUT")
    wm.add_argument("--max", type=int, default=1280); wm.add_argument("--crf", type=int, default=34)
    wm.set_defaults(func=cmd_webm)

    po = s.add_parser("poster"); po.add_argument("IN"); po.add_argument("OUT")
    po.add_argument("--time", type=float, default=0); po.set_defaults(func=cmd_poster)

    lo = s.add_parser("loop"); lo.add_argument("IN"); lo.add_argument("OUT")
    lo.add_argument("--xfade", type=float, default=0.5); lo.set_defaults(func=cmd_loop)

    pp = s.add_parser("pingpong"); pp.add_argument("IN"); pp.add_argument("OUT")
    pp.add_argument("--crf", type=int, default=30); pp.set_defaults(func=cmd_pingpong)

    a = p.parse_args(); a.func(a)


if __name__ == "__main__":
    main()
