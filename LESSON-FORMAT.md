# Lesson Format

Titled `0001-<dash-case-name>.html` in `./lessons/`. A lesson is one self-contained HTML file that teaches one tightly-scoped skill tied to the mission. Short, beautiful (Tufte-ish via `../assets/lesson.css`), completable in minutes. Each gives a single tangible win.

## Structure

Every lesson links `../assets/lesson.css` and (if interactive) `../assets/lesson.js` (deferred), then follows this skeleton:

```
<header class="lesson-head">
  <p class="kicker">Lesson NN · Phase X: Name</p>
  <h1>Title</h1>
  <p class="meta">From Dr. Justin Sung · "Video title"</p>
</header>

[content: knowledge — only what the skill needs]

[interactive: quiz / predict / guided widget — the skill practice]

<section class="recap">  one-sentence retrieval of the core idea
<section class="win">     the tangible thing you can now do
<section class="next">    links to next lesson(s) + reference doc(s)
<section class="teacher"> "Ask me anything that's unclear"
<span class="cite">        primary source link
```

## Interactive widgets (from `assets/lesson.js`)

### Quiz — multiple choice with answer reveal

```html
<details class="quiz" open data-answer="a" data-explain="Explanation shown on correct.">
  <summary class="quiz-prompt">Question?</summary>
  <div class="quiz-body">
    <div class="quiz-options">
      <label><input type="radio" name="q1" value="a"> Option A</label>
      <label><input type="radio" name="q1" value="b"> Option B</label>
    </div>
    <div class="quiz-feedback"></div>
    <div class="quiz-reveal"></div>
  </div>
</details>
```

### Predict — text input matching expected output

```html
<div class="predict" data-expected="expected answer">
  <p class="predict-prompt">Prompt?</p>
  <div class="predict-code">code or context</div>
  <input type="text" placeholder="Your answer…">
  <button>Check</button>
  <div class="predict-feedback"></div>
  <div class="predict-reveal"></div>
</div>
```

## Rules

- **One skill, one win.** Knowledge is only what that skill requires. The win is something you can *do*, not just understand.
- **Short.** Reads in ~5 min; practice ~2-5 min. No lesson covers a whole reference doc.
- **Equal-length quiz answers.** Every option is the same word count (and characters if possible) so formatting gives no clue.
- **Domain interleaving.** Examples alternate between front-end/freelancing, exams, and general life — for transfer and storage strength.
- **Link out.** Each lesson links to its reference doc(s) and adjacent lessons via `<a>`. Each recommends a primary source. Each closes with the teacher reminder.
- **Reuse components.** Before writing new code, check `assets/`. New reusable interactions go in `assets/`, never inline.
