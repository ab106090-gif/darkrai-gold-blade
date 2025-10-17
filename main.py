basic.show_icon(IconNames.PITCHFORK)
music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
    music.PlaybackMode.UNTIL_DONE)
mCar.rgb_light(mCar.McarRGBLight.RGBA, 0xff0000)
basic.show_leds("""
    # # . # #
    # # # # #
    . # . # #
    # # # # #
    # . # . #
    """)