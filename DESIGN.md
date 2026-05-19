# Design

> Zine digital de denuncia. Estética de panfleto fotocopiado / risografía a dos tintas. Light (papel), nunca dark. El medio es el argumento.

## Theme

Light. Escena que lo fuerza: *un estudiante proyecta este pasquín en un aula iluminada y luego se lee en laptop; tiene que leerse como una fotocopia pegada en un muro de la universidad, no como una app que brilla.* Papel envejecido, tinta densa. Dark mode no aplica: rompería la metáfora del documento impreso.

## Color

Estrategia: **Committed / dos tintas (risografía).** Papel + tinta carbón + una tinta de alarma. Sin tricolor patrio decorativo (la lectura colombiana viene de las voces y el contenido, no de la paleta). OKLCH.

- `--papel`: `oklch(0.928 0.013 83)` — hueso/fotocopia envejecida (fondo base).
- `--papel-sombra`: `oklch(0.880 0.016 80)` — papel manchado, para capas/recortes.
- `--tinta`: `oklch(0.205 0.014 55)` — carbón tibio, casi negro (texto, nunca #000).
- `--tinta-suave`: `oklch(0.430 0.018 55)` — gris de impresión gastada (metadatos, notas).
- `--rojo`: `oklch(0.560 0.205 27)` — rojo pasquín / segunda tinta (acusación, énfasis, sellos, números de panfleto). Carga 20–40% de las portadas.
- `--rojo-hueso`: `oklch(0.560 0.205 27 / 0.12)` — rojo bajo registro, manchas/resaltados.

Cada panfleto puede teñir levemente `--papel` (frío en P1 cuerpos, terroso en P2 tierra, profundo en P3 canto) sin salir del sistema de dos tintas. La portada (P0) puede ir *drenched* en rojo.

## Typography

Tres familias, cada una justificada por voz (no por reflejo). Cargadas self-hosted vía Fontsource o `@fontsource` en Astro; `font-display: swap`.

- **Titulares / manifestación — Big Shoulders Display.** Cara de señalética activista comunitaria, condensada, gritada. Tamaños enormes con `clamp()`, mayúsculas, tracking ceñido, peso 700–900. Es la voz que pega el cartel.
- **Cuerpo / testimonio — Petrona.** Serif contemporáneo latinoamericano, cálido y de expediente. Cuerpo del ensayo y citas en bloque. 1.125–1.25rem, medida 60–72ch, interlínea 1.6.
- **Etiquetas / pruebas / sellos — Special Elite.** Máquina de escribir: foliación de panfleto, referencias APA, pies de "documento/prueba", sellos (PROHIBIDO OLVIDAR, EXPEDIENTE). Sólo en piezas cortas; nunca cuerpo largo.

Escala modular ≥1.25. Las citas de las fuentes tienen jerarquía **mayor** que la prosa del autor: el testimonio se ve más grande que el análisis.

## Texture & Print system

La estética de fotocopia es estructural, va detrás del texto y nunca baja el contraste del cuerpo:

- Grano/ruido sutil (SVG `feTurbulence` o PNG tileable) en multiply sobre el papel.
- Desregistro de la segunda tinta: el rojo aparece desplazado 1–3px en sellos y titulares (efecto risografía mal alineada).
- Bordes de recorte/tijera y cinta para escaneos del cómic y páginas de Las Delicias/conscripción mostradas como "prueba".
- Sellos rotados (rotate -4deg a 6deg) con Special Elite y borde grueso.
- Reglas gruesas (3–6px) y filetes de carbón como separadores, no líneas de 1px tímidas.

## Layout

- **Navegación: panfletos como hojas separadas.** 5 rutas (P0 Portada/Manifiesto, P1 Los cuerpos reclutados, P2 La tierra robada, P3 El canto que no calla, P4 ¿Y ahora qué?). Anterior/Siguiente + índice de puntos `● ● ○ ● ●` fijo. Teclado (← →), swipe táctil. Astro View Transitions para el pase de hoja.
- Composición asimétrica, no centrada. Titulares desbordados, columnas rotas, collage de recortes y citas a sangre. Medida de cuerpo controlada (60–72ch) dentro del caos.
- Espaciado fluido `clamp()`, ritmo contrastado (respiros amplios entre bloques, agrupaciones tensas en el collage). Sin tarjetas iguales, sin contenedor por defecto.

## Motion

- Pase de panfleto: corte/desplazamiento seco tipo hoja arrancada (View Transitions), ease-out-expo, ~420ms. Sin bounce.
- Entrada por panfleto: titular y sello entran con stagger corto; el resto aparece sin coreografía que estorbe la lectura.
- Grano puede tener deriva muy lenta. Todo lo anterior se anula con `prefers-reduced-motion: reduce` (corte directo).

## Components

- **Sello** (stamp): Special Elite, borde 3px, rotado, color rojo o tinta.
- **Cita-testimonio**: bloque a mayor escala, atribución en Special Elite con referencia APA.
- **Pieza-prueba**: imagen de escaneo/cómic con marco de recorte, etiqueta de expediente y `alt` testimonial.
- **Folio/Indexador**: paginación de panfletos persistente.
- **Cabecera de panfleto**: número grande en rojo + título en Big Shoulders + bajada/tesis.
