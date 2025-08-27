# CSS
- [Fontes e formas de estilização](#fontes-e-formas-de-estilização)
- [Seletores e box model](#seletores-e-box-model)
- [Background](#background)
- [Flexbox](#flexbox)
## Fontes e formas de estilização

### Inline
```html
<span style="color:blue;">conteúdo</span>
```

### Tag `style`
```html
<style>
  div {
    font-size: 20px;
    font-weight: bold;
    font-style: italic;
  }
</style>

<div>conteúdo</div>
```

### Arquivo externo

```html
<!-- arquivo HTML -->
<link rel="stylesheet" href="./style.css">
```
```css
/* arquivo css */
button {
  font-family: "Gill Sans Extrabold", sans-serif;
}
```
[Voltar ao início](#css)

## Seletores e box model

```html
<!-- arquivo HTML -->
<h1 id="page-title">Título da página</h1>
<h2>Subtítulo</h2>
<div class="card">conteúdo</div>
```
```css
/* arquivo css */

#page-title {
  border: 1px solid  black;
  border-radius: 15px;
}

h2 {
  margin: 1em;
  padding: 5px;
}

.card{
  min-width: 300px;
  width: 80vw;
  max-width: 750px;
  min-height: 200px;
  height: 50vh;
  height: 500px;
}
```
[Voltar ao início](#css)

## Background

```css
span {
  background-color: lightgray;
}

.card {
  background-image: url('./assets/forest.png');
  background-size: cover;
}

section{
  background-image: linear-gradient(red, green, blue);
}
```
[Voltar ao início](#css)

## Flexbox

```css
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```
[Voltar ao início](#css)
