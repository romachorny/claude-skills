---
name: hebrew-rtl-copy-blocks
description: Make Hebrew text display correctly inside chat code blocks and copy boxes, where punctuation jumps to the wrong end and mixed Hebrew and English words swap places. Wraps every Hebrew line in invisible direction marks and applies layout rules for Latin words, numbers and links. Use whenever Hebrew (or Arabic) text goes into a code block, a copy box or a message field.
---

# Hebrew RTL in copy blocks

A chat code block is always left-to-right. Hebrew inside it breaks: the full stop and the question mark land at the start of the line, and a Latin word in the middle of a sentence swaps places with its neighbours. The reader sees a broken message and cannot tell whether it will arrive broken too.

Built after one day in which the same Hebrew note came out "from the wrong side" three times.

## Fix: direction marks on every line

Wrap EVERY Hebrew line in two invisible characters:

- RLE, U+202B (Right-to-Left Embedding) at the start of the line
- PDF, U+202C (Pop Directional Formatting) at the end of the line

The block then lays out each line right to left, and punctuation sits at the end of the sentence. The characters are invisible and survive copy and paste into WhatsApp, LinkedIn, Gmail and Telegram.

Do not wrap empty lines or lines that contain only a link.

`scripts/rtl_wrap.py` does this for you:

```bash
python scripts/rtl_wrap.py < message.txt > message_rtl.txt
```

## Layout rules

1. Replace Latin words with Hebrew where a Hebrew word exists: "משאבי אנוש", not "HR".
2. A Hebrew line never starts or ends with a Latin word, a number or a link. Rebuild the sentence so the Latin word sits in the middle.
3. A link sits alone on its own line, with no punctuation before or after it. No "תודה:" before it, no full stop after it.
4. No full stop, colon or bracket right after a Latin word or a link.
5. Brand names (Claude, LinkedIn, WhatsApp) only in the middle of a Hebrew phrase. A prefix letter glued to a Latin word ("ב", "ו", "ל") breaks the order: rebuild the phrase instead.
6. Phone numbers are written as one run of digits, no spaces or dashes.

## Pasting into a message field

When the agent pastes the text into an open chat box for the person to send, insert it as text (for example `document.execCommand('insertText', false, text)`), check that it reads right to left in the field, and never press Send. The human sends.

## Check before handing over

- Every Hebrew line starts with U+202B and ends with U+202C.
- No line starts or ends with Latin, digits or a link.
- Read the block on a phone screen width: the question mark is on the left end of the line.
