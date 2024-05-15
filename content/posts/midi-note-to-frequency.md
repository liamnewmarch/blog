---
date: 2023-06-11
title: MIDI note to frequency
summary: How to determine the frequency of a note on a piano.
image:
  url: /posts/img/midi-note-to-frequency.avif
  width: 1280
  height: 853
---

The [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) gives you access to low-level primitives for [sound synthesis](https://en.wikipedia.org/wiki/Synthesizer). It’s a lot of fun to play with and you don’t need to be an audio scientist in order to make bloopy noises, but if you want to make something musical, you’ll soon find that maths, physics and music theory come into play.

With the [Root](https://gitlab.com/potato-oss/web-audio/root) audio component library, we tried to solve some of these problems for web developers by wrapping the Web Audio primitives in Web Components. In this article I’m going to take a closer look at one of the problems that we solved.

## No notes

One aspect of the Web Audio API that may trip up muscians is that it has no concept of notes. Instead, oscillators, the basic building block for synthesis, use frequencies specified in Hz.

There is a handy Wikipedia page for [piano keys frequencies](https://en.wikipedia.org/wiki/Piano_key_frequencies) with formulae and even a table of values we can use for reference. I stumbled upon this page years ago and, after tweaking the values slightly to suit my needs, settled on this formula for converting a note into a frequency:

```js
let frequency = 2 ** ((note - 69) / 12) * 440
```

Let’s break that down.

* `frequency` is the number in Hz we’re trying to find for a given input `note`.
* `note` is the integer number of the key being pressed according to [General MIDI](https://en.wikipedia.org/wiki/General_MIDI).
* `440` is the [standard frequency](https://en.wikipedia.org/wiki/A440_(pitch_standard)) in Hz for the key A4.
* `69` is the MIDI note number for the key A4.
* `12` refers to the number of tones in an octave.

And raising the whole thing to a power of `2` is the magic part. This is what makes the graph this formula produces a curve such that A4 is double the frequency of A3, and C3 is double the frequency C2.

If you wanted to wrap this in a function that supports transposition, tuning, and even changing the number of tones in an octave, try this:

```ts
export const A4_NOTE = 69

export function noteToFrequency(note, {
  tones = 12,
  transpose = 0,
  tuning = 440,
} = {}) {
  return 2 ** ((note - A4_NOTE + transpose) / tones) * tuning
}
```

## Wrapping up

I could go on. There’s so much to talk about, like how these frequencies are [a compromise](https://en.wikipedia.org/wiki/Equal_temperament) that don’t [align with nature](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)) but that sound good enough to our ears… but that’s an article for a another day.
