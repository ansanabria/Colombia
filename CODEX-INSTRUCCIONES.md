# Brief exhaustivo para Codex — 5 pósters del zine "Memoria y Violencia"

Archivo autocontenido. Describe **cada imagen píxel a píxel**: posición, tamaño, color y contenido textual literal de cada elemento. Un modelo de imagen debe poder producir el resultado casi final siguiendo esto. No reescribas textos: son citas de un ensayo académico.

---

## 0. Cómo usar este archivo

- **Salida:** 5 PNG, **1680 × 1050 px exactos**, en:
  `/home/andy-spike/Documents/Uni/Colombia/posters/p0.png … p4.png` (crea `posters/` si falta; no toques nada fuera de ahí).
- **Método:** usa tu generación de imágenes. Genera **primero `p0.png` (piloto)** y deja constancia del comando/herramienta. Si el piloto sirve, genera los 5.
- **Si NO puedes generar ráster:** no simules ni dejes placeholders; detente y reporta qué intentaste, qué herramientas/APIs/credenciales hay y qué falta.
- **P2 es composición real:** genera el cartel tipográfico y **incrusta por código** los 3 PNG del cómic indicados (no los redibujes).
- **Reporte final:** método exacto, lista de archivos + dimensiones reales, desviaciones/limitaciones.

---

## 1. Especificación global (aplica a los 5)

### 1.1 Lienzo y rejilla

- Lienzo 1680 × 1050 px. Origen (0,0) arriba-izquierda. Todas las coordenadas en px.
- **Margen de seguridad:** 64 px por lado. Caja de contenido = x∈[64,1616], y∈[64,986].
- **Franja de navegación inferior reservada:** y∈[986,1050] (64 px). El contenido principal no invade esta franja salvo sangrados decorativos.
- Permitido y deseado que **titulares e ilustraciones sangren** fuera del lienzo por los bordes superior/lateral (corte intencional).

### 1.2 Paleta (no usar otros colores)

| Rol | Hex | Uso |
|---|---|---|
| Papel | `#ECE5D6` | Fondo base (P1–P4) y texto sobre rojo (P0) |
| Papel mancha | `#DCD3BD` | Capas, sombras de papel, cinta |
| Tinta | `#211C16` | Texto y trazo principal (nunca negro puro) |
| Tinta gastada | `#574E40` | Metadatos, pies, texto secundario |
| Rojo pasquín | `#CC2F26` | 2ª tinta: folio, sellos, énfasis, acusación |
| Rojo profundo | `#9B241D` | Solo fondo drench de P0 |

### 1.3 Tipografía (Google Fonts; pesos y px exactos)

- **Big Shoulders Display** (titulares, folio, cifras): mayúsculas, peso 800–900, condensado, tracking −1%.
- **Petrona** (cuerpo, tesis, citas): serif; citas en itálica; peso 400–600.
- **Special Elite** (máquina de escribir): sellos, foliación pequeña, pies de imagen, etiquetas de expediente, referencias APA, franja de navegación. Solo piezas cortas.

Escala base (ajusta ±10% para encajar sin desbordar de forma fea):

| Elemento | Fuente | Tamaño px | Interlineado |
|---|---|---|---|
| Folio (00–04) | Big Shoulders 900 | altura de mayúscula ≈ 300 | — |
| Titular de panfleto | Big Shoulders 800 | 110–200 | 0.9 |
| Palabra-grito (P0 "EXPLOTACIÓN", P4 sentencia) | Big Shoulders 900 | 210–300 | 0.86 |
| Bajada/itálica | Petrona italic 500 | 32–38 | 1.3 |
| Cuerpo/tesis | Petrona 400 | 26–30 | 1.45 |
| Cita-testimonio | Petrona italic 500 | 50–72 | 1.12 |
| Cifra brutal (P1) | Big Shoulders 900 | 220–300 | 0.8 |
| Sello | Special Elite 400 | 28–40 | 1.05 |
| Pie de imagen / etiqueta | Special Elite 400 | 20–24 | 1.3 |
| Franja navegación | Special Elite 400 | 22 | — |

### 1.4 Texturas y "impresión" (obligatorio en los 5)

- **Grano de fotocopia** sobre todo el lienzo: ruido monocromo fino en modo multiply, opacidad 8–12%.
- **Desregistro risográfico:** cada elemento en rojo se duplica desplazado 2–4 px (típico +3,+2) en una capa que asoma; bordes de tinta ligeramente "corridos", no perfectos.
- **Manchas/viñeteado** muy sutil de fotocopia en las esquinas (oscurecimiento 6–10%).
- **Filetes:** reglas gruesas de 4–6 px en tinta como separadores; nunca líneas de 1 px.
- **Bordes ásperos:** títulos y sellos con borde ligeramente erosionado (no vectorial perfecto), efecto linóleo/fotocopia.

### 1.5 Sello (construcción exacta)

Caja rectangular con **borde de 3 px** del color del sello (rojo `#CC2F26` salvo que se indique tinta), texto Special Elite mayúsculas dentro, padding 14 px, **rotación entre −6° y +6°**, tinta saltada/gastada (10–20% del trazo ausente), ligero doble registro rojo. Sin relleno de fondo (deja ver el papel).

### 1.6 Folio (esquina superior izquierda, los 5)

Número de 2 dígitos (`00`…`04`) en Big Shoulders 900, altura ≈ 300 px, color rojo `#CC2F26`, con **fantasma en tinta** desplazado −4,−3 px al 18% de opacidad. Esquina: x≈64, borde superior sangrando ligeramente fuera (y≈ −10 a 300). Es el elemento más grande tras el titular.

### 1.7 Franja de navegación inferior (los 5, idéntica)

- Banda y∈[986,1050], fondo papel `#ECE5D6` (en P0 también papel, no rojo), separada del contenido por un **filete de 6 px en tinta** en y=986.
- Contenido en Special Elite 22 px, tinta, mayúsculas, tracking +5%:
  - Izquierda (x≈64): `← ANTERIOR` (en P0 atenuado al 28%, es el primero).
  - Centro: 5 puntos ⌀14 px, separación 28 px, borde tinta 2 px; el del panfleto actual **relleno rojo**. Estados: P0 `●○○○○`, P1 `○●○○○`, P2 `○○●○○`, P3 `○○○●○`, P4 `○○○○●`.
  - Derecha (x≈1616, alineado a la derecha): `SIGUIENTE →` (en P4 cambia a `VOLVER AL MANIFIESTO ↺`).
  - Extremo derecho, más pequeño (18 px, tinta gastada): `PANFLETO 0X / 04`.

### 1.8 Prohibido (negative prompt)

Fotorrealismo de víctimas o de la masacre real; gradientes suaves; glassmorphism; tarjetas iguales con iconos; hero centrado tipo SaaS; estética de museo pulcra y conciliadora; brillo; emojis; banderas/colores fuera de la paleta; texto mal escrito o sin tildes; marcas de agua; firmas; logos de stock.

---

## 2. PÓSTER POR PÓSTER

> Coordenadas como guía de composición (no tienen que ser exactas al píxel, pero sí respetar zonas, jerarquía y proporciones). El **texto va literal**.

---

### P0 — Portada / Manifiesto → `posters/p0.png`

**Concepto:** el cartel pegado al muro que abre el zine; agresivo, declarativo.
**Fondo:** drench completo **rojo profundo `#9B241D`** con grano y viñeteado. Tipografía en papel `#ECE5D6` y, donde se indica, sobre franjas de papel con texto en tinta.

Composición (de arriba abajo):

1. **Crédito** — caja x[64,560] y[64,150]. Special Elite 24 px, papel, mayúsculas, 3 líneas, con un filete papel de 4 px encima:
   `ELECTIVA «COLOMBIA»` / `EJE: MEMORIA Y VIOLENCIA` / `PROYECTO FINAL · ENSAYO VISUAL`
2. **Sello** — esquina sup. der., centro ≈ (1500,110), rotado +5°, borde papel 3 px, texto papel: `PROHIBIDO OLVIDAR`.
3. **Folio** `00` rojo desregistrado, x≈64, y≈ −10..300 (sangra arriba), sobre el rojo el folio va en **papel** con fantasma tinta (excepción: en fondo rojo el folio es papel, no rojo).
4. **Titular** — bloque y[300,720], x desde 56 sangrando a la derecha. Big Shoulders, papel:
   - Línea 1 (peso 700, ≈110 px): `RADIOGRAFÍA`
   - Línea 2 (≈64 px, tracking +8%, opacidad 70%): `DE LA`
   - Línea 3 (peso 900, ≈300 px, se corta en el borde derecho del lienzo): `EXPLOTACIÓN` con fantasma tinta desplazado +5,+4.
5. **Tesis** — franja de papel `#ECE5D6` x[64,980] y[740,900], texto tinta Petrona 28 px, con la frase clave en negrita:
   «Las minorías en Colombia no fueron marginalizadas y explotadas por accidente. Lo fueron por estructuras de poder que sirven a intereses del capital. La explotación de los cuerpos jóvenes, el despojo de la tierra campesina y la destrucción de las comunidades negras **son tres caras de un mismo proceso**: heredado del colonialismo, acelerado por el neoliberalismo.»
6. **Índice** — x[64,1616] y[904,980], Special Elite 24 px, papel; números en rojo; separadores `·`:
   `01 LOS CUERPOS RECLUTADOS · 02 LA TIERRA ROBADA · 03 EL CANTO QUE NO CALLA · 04 ¿Y AHORA QUÉ?`
7. **Franja de navegación** (§1.7) estado `●○○○○`, `← ANTERIOR` atenuado, derecha `SIGUIENTE →`, `PANFLETO 00 / 04`.

---

### P1 — Los cuerpos reclutados → `posters/p1.png`

**Concepto:** el Estado selecciona por clase qué cuerpos son carne de cañón.
**Fondo:** papel `#ECE5D6` con tinte frío muy sutil; grano.

**Ilustración (linograbado / cartel agitprop a 2 tintas, negro `#211C16` + rojo `#CC2F26`; NO foto, NO documento):**
Ocupa la mitad inferior-izquierda, caja aprox x[40,940] y[470,1000], puede sangrar por abajo/izquierda. Escena, descrita en detalle:
- **Plano medio-largo en diagonal** que sube de abajo-izquierda hacia arriba-derecha: una **columna densa de jóvenes reclutas pobres** (10–14 figuras), siluetas macizas en negro, cabezas rapadas o con gorra de cuartel, morrales/petates al hombro, ropa humilde, todos de espalda o de perfil avanzando; las figuras se hacen más pequeñas hacia el fondo (perspectiva).
- Al final de la fila, arriba-derecha de la ilustración, la **reja/portón de un cuartel precario** de tablones en plena selva; sobre el portón una **bandera/triángulo rojo** y un asta. Detrás, masas negras de selva (frondas dentadas) que aplastan la escena.
- En primer plano abajo-izquierda, separada por una reja, una **figura de élite** (silueta con saco, sentada a un escritorio) que entrega/recibe una **libreta militar roja**: representa a quien paga y no entra. Contraste de clase explícito.
- Tratamiento: alto contraste, masas negras planas, **textura de gubia** (líneas talladas blancas/papel sobre los negros), bordes erosionados, registro del rojo ligeramente corrido. Sin rostros detallados (siluetas), digno, no gore.

**Texto y datos (mitad superior y columna derecha, sin pisar la ilustración):**
1. **Folio** `01` rojo gigante desregistrado, sup. izq. (x≈64, y −10..300).
2. **Titular** Big Shoulders tinta, a la derecha del folio, ≈140 px, 2 líneas: `LOS CUERPOS` / `RECLUTADOS`.
3. **Bajada** Petrona itálica 36 px, tinta gastada, ≤46 car., bajo el titular:
   «El servicio militar obligatorio no es defensa nacional: es extracción de cuerpos jóvenes y pobres como carne de cañón.»
4. **Filete** tinta 6 px a todo el ancho bajo la cabecera (y≈360).
5. **Dato brutal** — bloque derecho x[1000,1616] y[400,720]: `80%` en Big Shoulders 900 rojo ≈ 280 px con fantasma tinta; debajo, tinta Big Shoulders 700 ≈ 40 px: `DE LOS RECLUTAS SON ESTRATO 0, 1 Y 2`; al lado, menor, tinta gastada: `0,01% SON ESTRATO 6`. Pie Special Elite 22 px: `DEFENSORÍA DEL PUEBLO, 2014 — EN SANTAEULALIA, 2022`.
6. **Cita-testimonio** — sobre franja de papel, x[980,1616] y[740,940], Petrona itálica 56 px con comilla roja descomunal:
   «En Colombia el servicio militar es obligatorio solo para el que no puede pagarlo.»
   Atribución Special Elite 22 px: `— SANTAEULALIA, EL PAÍS, 2022`.
7. **Sello** rojo rotado −5°, centro ≈ (1480,420): `CARNE DE CAÑÓN`.
8. **Franja de navegación** estado `○●○○○`.

---

### P2 — La tierra robada → `posters/p2.png`  ·  COMPONE LOS 3 PNG DEL CÓMIC

**Concepto:** tablero de evidencias del despojo cotidiano.
**Fondo:** papel `#ECE5D6` con tinte terroso cálido; grano.

**Imágenes fuente a INCRUSTAR por código (no redibujar). Tratar en blanco y negro de alto contraste (grayscale + contraste +40%), como clippings recortados con tijera (borde irregular), con un trozo de cinta `#DCD3BD` translúcida y rotación leve. Dimensiones reales entre paréntesis:**

| Archivo | (px reales) | Caja destino aprox. | Rotación |
|---|---|---|---|
| `/home/andy-spike/Documents/Uni/Colombia/public/img/comic/palma-carros.png` | (590×1170, vertical) | x[80,470] y[470,980] | −4° |
| `/home/andy-spike/Documents/Uni/Colombia/public/img/comic/desplazamiento.png` | (950×1220) | x[470,980] y[430,940], puede sangrar | +3° |
| `/home/andy-spike/Documents/Uni/Colombia/public/img/comic/campesina.png` | (975×1240) | x[1120,1600] y[520,1000] | +5° |

Pie Special Elite 20 px bajo cada recorte (tinta), con flecha roja `▸`:
- palma-carros → `Casas campesinas y carros del agronegocio entrando entre la palma.`
- desplazamiento → `Una mano tacha el territorio; la gente carga lo que puede y se va.`
- campesina → `Quien se queda resiste, rodeada de palma y de miedo.`

**Texto:**
1. **Folio** `02` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈170 px a la derecha del folio: `LA TIERRA ROBADA`.
3. **Bajada** Petrona itálica 36 px tinta gastada: «El despojo no terminó con la guerra: se volvió legal, lento y cotidiano.»
4. **Filete** tinta 6 px (y≈330).
5. **Cita dominante** — franja de papel opaca cruzando el centro sobre los recortes, x[470,1140] y[560,760], Petrona itálica 60 px, comilla roja:
   «La palma no quiere yuca, ni plátano, ni maíz cerca, quiere estar sola.»
   Atribución Special Elite 22 px: `— RAMIRO, CAMPESINO DE OVEJAS · OJEDA ET AL., 2015, P. 116`.
6. **Sello** rojo rotado +6°, centro ≈ (1480,360): `DESIERTO VERDE`.
7. **Etiqueta de expediente** Special Elite 20 px, esquina inf. izq. sobre el primer recorte:
   `FUENTE: CAMINOS CONDENADOS · OJEDA, GUERRA, AGUIRRE, DÍAZ · 2016`.
8. **Franja de navegación** estado `○○●○○`.

---

### P3 — El canto que no calla → `posters/p3.png`

**Concepto:** el duelo afro convertido en denuncia política; dignidad, no lástima.
**Fondo:** papel `#ECE5D6` con tinte profundo muy sutil; grano.

**Ilustración (linograbado a 2 tintas, sobria y digna; NO caricaturesca; NO explotar el dolor):**
Caja aprox x[860,1660] y[300,1000], sangra por la derecha/abajo. Escena:
- **Tres a cinco mujeres afrocolombianas de pie, cantando** (las alabaoras de Pogue): siluetas negras macizas, **bocas abiertas en canto**, cabezas en alto, pañuelos/turbantes, vestidos largos; postura de fuerza colectiva, hombro con hombro, no de derrota.
- Detrás, el **río Atrato** y la selva del Chocó en masas negras simplificadas; una iglesia pequeña al fondo (alusión a Bellavista) sin dramatismo explícito.
- Saliendo de las bocas, **ondas/nota roja `#CC2F26`** que cruzan hacia la izquierda y se hacen grandes (la voz que viaja y llega lejos); el rojo desregistrado.
- Textura de gubia, alto contraste, bordes erosionados. Sin rostros detallados; gesto y postura, no sangre.

**Texto (mitad izquierda):**
1. **Folio** `03` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈150 px, 2 líneas: `EL CANTO` / `QUE NO CALLA`.
3. **Bajada** Petrona itálica 36 px tinta gastada: «Bojayá enterró a sus muertos cantando: el duelo se volvió denuncia.»
4. **Filete** tinta 6 px (y≈360).
5. **Cita-testimonio** dominante, x[64,860] y[430,820], Petrona itálica 52 px, comilla roja:
   «Compongo por las situaciones que estamos viviendo, pa’ ver si esos dolores le llegan también allá al presidente. Porque nosotros los campesinos somos los que pagamos los platos rotos de los actores armados.»
   Atribución Special Elite 22 px: `— ONEIDA OREJUELA, ALABAORA · QUICENO TORO ET AL., 2017, P. 185`.
6. **Sello** en **tinta** (no rojo) rotado −5°, centro ≈ (300,900): `GUAYACÁN DE LA COMUNIDAD`.
7. **Franja de navegación** estado `○○○●○`.

---

### P4 — ¿Y ahora qué? → `posters/p4.png`

**Concepto:** cierre desnudo y brutal; no consuela, interpela.
**Fondo:** papel `#ECE5D6`; grano; el más tipográfico y vacío (espacio negativo deliberado).

1. **Folio** `04` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈150 px a la derecha del folio: `¿Y AHORA QUÉ?`.
3. **Filete** tinta 6 px (y≈330).
4. **Sentencia descomunal** — centro del lienzo, x[64,1616] y[360,720], Big Shoulders mayúsculas, 2 partes:
   - En tinta, peso 700, ≈80 px: `LA EXPLOTACIÓN DE LAS MINORÍAS NO ES UN CAPÍTULO CERRADO DEL CONFLICTO.`
   - Debajo, en **rojo `#CC2F26`** peso 900, ≈230 px, con fantasma tinta desregistrado, sangrando a los lados: `ES EL MOTOR DEL SISTEMA.`
5. **Pregunta incómoda** — bloque x[64,900] y[740,940], Petrona 28 px tinta:
   «Si el sistema de explotación es estructural, si viene de lejos, si se moderniza pero no desaparece, ¿qué transformación real es posible? La respuesta no está en este texto: está en las organizaciones campesinas, en los movimientos indígenas y afro, en las mujeres que cantan alabao a pesar del miedo.»
6. **Sello** rojo grande rotado +5°, centro ≈ (1380,820): `¿Y AHORA QUÉ?`.
7. **Expediente de fuentes** — Special Elite 20 px, tinta gastada, x[64,1616] y[946,980]:
   `HOYOS 1997 · OJEDA ET AL. 2015 · QUICENO TORO ET AL. 2017 · RODRÍGUEZ HERNÁNDEZ 2008 · QUIJANO 2000 · HARVEY 2005`.
8. **Franja de navegación** estado `○○○○●`; a la derecha `VOLVER AL MANIFIESTO ↺`; `PANFLETO 04 / 04`.

---

## 3. Prompts sugeridos por póster (si generas por texto→imagen)

Úsalos como prompt base; el copy literal y las cajas mandan sobre el prompt. Estilo común a anteponer en los 5:

> *Cartel político de pasquín fotocopiado, risografía a dos tintas, estética de taller de serigrafía latinoamericano y agitprop años 70-80, grano de fotocopia, registro de tinta roja ligeramente corrido, bordes erosionados, composición editorial asimétrica, tipografía condensada de manifestación, papel hueso #ECE5D6, tinta #211C16, rojo #CC2F26. Sin fotorrealismo, sin gradientes, sin brillo, sin glassmorphism, sin logos.*

- **P0:** *fondo rojo profundo #9B241D drench, gran titular tipográfico en papel "RADIOGRAFÍA DE LA EXPLOTACIÓN" con la última palabra descomunal cortándose en el borde, franja de papel con párrafo de tesis, índice mecanografiado, sello "PROHIBIDO OLVIDAR". Solo tipografía, sin ilustración.*
- **P1:** *linograbado a 2 tintas: columna diagonal de jóvenes reclutas pobres en silueta negra con petates marchando hacia la reja de un cuartel de tablones en la selva con bandera roja; en primer plano, separada por una reja, una figura de saco que paga una libreta roja; masas negras de selva al fondo; textura de gubia; alto contraste; cifra tipográfica enorme "80%" en rojo a la derecha.*
- **P2:** *tablero de evidencias: collage de tres recortes de cómic en blanco y negro (se incrustan aparte) con cinta y rotación, gran cita en cursiva sobre franja de papel cruzando el centro, sello "DESIERTO VERDE", etiqueta de expediente mecanografiada.*
- **P3:** *linograbado a 2 tintas, digno y sobrio: tres a cinco mujeres afrocolombianas de pie cantando en silueta negra, bocas abiertas, río Atrato y selva al fondo, ondas de sonido rojas saliendo de las bocas y viajando lejos; sin sangre, postura de fuerza colectiva.*
- **P4:** *cartel tipográfico desnudo, mucho espacio en papel, sentencia descomunal "ES EL MOTOR DEL SISTEMA" en rojo con fantasma de tinta corrido, párrafo de pregunta en serif, sello "¿Y AHORA QUÉ?".*

---

## 4. Checklist QA (por póster, antes de entregar)

- [ ] 1680×1050 px exactos. Solo la paleta de §1.2.
- [ ] Folio gigante rojo desregistrado sup. izq.; franja de navegación inferior con el punto correcto y textos de §1.7.
- [ ] Titular en Big Shoulders, cuerpo/cita en Petrona, etiquetas/sellos en Special Elite.
- [ ] Copy **literal**, con tildes y «comillas» correctas; sin texto inventado ni recortado a media palabra.
- [ ] Grano de fotocopia + desregistro rojo visibles; filetes de 4–6 px; sellos rotados con tinta saltada.
- [ ] P0 fondo rojo profundo; P4 tipográfico con espacio negativo; P1 y P3 con ilustración linograbado original (siluetas, sin gore, dignas).
- [ ] P2 incrusta REALMENTE los 3 PNG del cómic indicados, en B/N alto contraste, con cinta, rotación y su pie.
- [ ] Composición asimétrica, sangrados intencionales, jerarquía clara (folio/titular → cita/dato → cuerpo → pies).
- [ ] Reporte final: método exacto, archivos + dimensiones, desviaciones/limitaciones.
