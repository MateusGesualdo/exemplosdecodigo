# Exemplos de Código
## Índice
- HTML
  - [Estrutura básica](#estrutura-básica)
  - [Títulos e subtítulos](#títulos-e-subtítulos)
  - [Parágrafos](#parágrafos)
  - [Hiperlinks](#hiperlinks)
  - [Imagens](#imagens)
  - [Listas](#listas)
  - [Formulários](#formulários)
  - [Tabelas](#tabelas)
  - [Contêineres genéricos](#contêineres-genéricos)
  - [Elementos semânticos](#elementos-semânticos)
- CSS
  - [Fontes e formas de estilização](#fontes-e-formas-de-estilização)
  - [Seletores e box model](#seletores-e-box-model)
  - [Background](#background)
  - [Flexbox](#flexbox)

### HTML

#### Estrutura básica
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Texto na aba da página</title>
</head>
<body>
  
</body>
</html>
```
[Voltar ao índice](#índice)

#### Títulos e subtítulos
```html
<h1>Conteúdo do título 1</h1>
<h2>Conteúdo do título 2</h2>
<h3>Conteúdo do título 3</h3>
<h4>Conteúdo do título 4</h4>
<h5>Conteúdo do título 5</h5>
<h6>Conteúdo do título 6</h6>
```
[Voltar ao índice](#índice)

#### Parágrafos
```html
<p>Conteúdo do parágrafo</p>
```
[Voltar ao índice](#índice)

#### Hiperlinks
```html
<a href="./about.html">Texto do hiperlink</a>
<!-- link para outro arquivo na mesma pasta -->
 
<a href="https://github.com" target="_blank">
  Visite meu perfil no Github
</a>
<!-- link para outro website (abre numa nova aba) -->

<h1 id="page-title">Título da página</h1>
<a href="#page-title"></a>
<!-- link para outro elemento na mesma página -->
```
[Voltar ao índice](#índice)

#### Imagens
```html
<img src="./assets/logo.png" alt="texto alternativo"/>
```
[Voltar ao índice](#índice)

#### Listas
```html
<ol>
  <li>Primeiro item</li>
  <li>Segundo item</li>
  <li>Terceiro item</li>
</ol>
<!-- Lista ordenada -->

<ul>
  <li>Primeiro item</li>
  <li>Segundo item</li>
  <li>Terceiro item</li>
</ul>
<!-- Lista sem ordenação -->

```
[Voltar ao índice](#índice)

#### Formulários
```html
<form>
  
  <label for="username">Nome:</label>
  <input id="username">

  <label for="email">Email:</label>
  <input type="email" id="email">

  <input type="checkbox" id="accept-tos">
  <label for="accept-tos">
    Li e aceito os Termos de Serviço
  </label>

  <textarea placeholder="Escreva uma mensagem"></textarea>  

  <input type="submit" value="Enviar">

</form>
```
[Voltar ao índice](#índice)

#### Tabelas
```html
<table>
  
  <caption>Legenda da tabela</caption>
  
  <thead>
    <tr>
      <th></th>
      <th>Coluna A</th>
      <th>Coluna B</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <th>Linha 1</th>
      <td>Célula 1A</td>
      <td>Célula 2A</td>
    </tr>
    <tr>
      <th>Linha 2</th>
      <td>Célula 1B</td>
      <td>Célula 2B</td>
    </tr>   
  </tbody>
  
  <tfoot>
    <tr>
      <th colspan="3">rodapé</th>
    </tr>
  </tfoot>

</table>
```
[Voltar ao índice](#índice)

#### Contêineres genéricos

```html
<span>Conteúdo do span</span>
<!-- conteiner em linha -->

<div>Conteúdo da div</div>
<!-- conteiner em bloco -->
```
[Voltar ao índice](#índice)

#### Elementos semânticos

```html
<!-- Alguns dos aproximadamente 100 elementos semânticos disponíveis: -->

<header>Cabeçalho</header>

<main>Conteúdo principal do body</main>

<footer>Rodapé</footer>

<nav>Menu de navegação</nav>

<section>Seção genérica</section>

<details>
  <summary>"Saiba mais"</summary>
  Conteúdo dentro de um dropdown
</details>

<figure>
  <figcaption>Legenda da figura</figcaption>
</figure>
```
[Voltar ao índice](#índice)

#### `<iframe>` (Inline Frame)

```html
<iframe 
  src="https://www.youtube.com/embed/5fQOIllQywE"
  title="Por Que a Torre de Pisa Está Inclinada? Descubra a História Surpreendente! #torredepisa" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>
<!-- vídeo do YouTube  -->

 <iframe 
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2883.4031148805516!2d10.394022076180502!3d43.72295197109896!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12d591a6c44e88cd%3A0x32eca9b1d554fc03!2sTorre%20de%20Pisa!5e0!3m2!1spt-BR!2sbr!4v1755877325109!5m2!1spt-BR!2sbr" 
  width="600" 
  height="450" 
  style="border:0;" 
  allowfullscreen="" 
  loading="lazy" 
  referrerpolicy="no-referrer-when-downgrade">
</iframe>
<!-- mapa do Google -->

```
[Voltar ao índice](#índice)

### CSS

#### Fontes e formas de estilização

1. Inline
    ```html
    <span style="color:blue;">conteúdo</span>
    ```

1. Tag `style`
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

1. Arquivo externo

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
[Voltar ao índice](#índice)

#### Seletores e box model

```html
<!-- arquivo HTML -->
<h1 id="page-title">Título da página</h1>
<div class="card">conteúdo</div>
```
```css
/* arquivo css */

#page-title {
  border: 1px solid  black;
  border-radius: 15px;
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
[Voltar ao índice](#índice)

#### Background

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
[Voltar ao índice](#índice)

#### Flexbox

```css
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```
[Voltar ao índice](#índice)
