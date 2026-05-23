# Brief exhaustivo para Codex — 6 panfletos del zine "Memoria y Violencia"

Archivo autocontenido. Describe **cada imagen píxel a píxel**: posición, tamaño, color y contenido textual literal de cada elemento. Un modelo de imagen debe poder producir el resultado casi final siguiendo esto. No reescribas textos: son citas de un ensayo académico real.

---

## 0. Cómo usar este archivo

- **Salida:** 6 PNG, **1680 × 1050 px exactos**, en:
  `/home/andy-spike/Documents/Uni/Colombia/posters/p0.png … p5.png` (crea `posters/` si falta; no toques nada fuera de ahí).
- **Método:** usa tu generación de imágenes. Genera **primero `p0.png` (piloto)** y deja constancia del comando/herramienta. Si el piloto sirve, genera los 6.
- **Si NO puedes generar ráster:** no simules ni dejes placeholders; detente y reporta qué intentaste, qué herramientas/APIs/credenciales hay y qué falta.
- **P3 usa imágenes del cómic como referencia visual:** antes de generar P3, abre los 3 PNG indicados en la sección de P3, obsérvalos y replícalos con generación de imágenes dentro del cartel. No insertes nada por código.
- **Reporte final:** método exacto, lista de archivos + dimensiones reales, desviaciones/limitaciones.

---

## 1. Especificación global (aplica a los 6)

### 1.1 Lienzo y rejilla

- Lienzo 1680 × 1050 px. Origen (0,0) arriba-izquierda. Todas las coordenadas en px.
- **Margen de seguridad:** 64 px por lado. Caja de contenido = x∈[64,1616], y∈[64,986].
- **Franja de navegación inferior reservada:** y∈[986,1050] (64 px). El contenido principal no invade esta franja salvo sangrados decorativos.
- Permitido y deseado que **titulares e ilustraciones sangren** fuera del lienzo por los bordes superior/lateral (corte intencional).

### 1.2 Paleta (no usar otros colores)

OKLCH es la fuente de verdad (de `DESIGN.md`); el hex acompaña para uso directo en generación de ráster. Nunca usar negro puro `#000` ni blanco puro `#fff` (rompen la metáfora del documento impreso).

| Rol | Hex | OKLCH | Uso |
|---|---|---|---|
| Papel | `#ECE5D6` | `oklch(0.928 0.013 83)` | Fondo base (P1–P5) y texto sobre rojo (P0) |
| Papel mancha | `#DCD3BD` | `oklch(0.880 0.016 80)` | Franjas detrás de cita de apoyo, cinta, capas, sombras de papel |
| Tinta | `#211C16` | `oklch(0.205 0.014 55)` | Texto y trazo principal (carbón tibio, nunca `#000`) |
| Tinta gastada | `#574E40` | `oklch(0.430 0.018 55)` | Metadatos, pies, atribuciones, grano tintado |
| Rojo pasquín | `#CC2F26` | `oklch(0.560 0.205 27)` | 2ª tinta: folio, sellos, énfasis, acusación |
| Rojo profundo | `#9B241D` | `oklch(0.470 0.180 27)` | Solo fondo drench de P0 |

**Estrategia de color:** *Committed / risografía a dos tintas.* La paleta es de 6 valores y no admite ampliación. Sin tricolor patrio decorativo. La carga del rojo en los panfletos interiores está entre 12% y 25% de la superficie; en P0 es drench.

**Tinte sutil del papel por panfleto** (desviación ≤4% del papel base, no se siente como cambio de paleta sino como voz):

| Panfleto | Hex de fondo | Justificación |
|---|---|---|
| P0 | `#9B241D` (drench) | Portada: acusación inmediata. |
| P1 | `#ECE5D6` | Expediente neutro: postura sostenida. |
| P2 | `#E8E5DE` | Frío sutil: Putumayo, abandono. |
| P3 | `#EDE2CC` | Ocre terroso: tierra arrebatada de Montes de María. |
| P4 | `#E5DCC9` | Húmedo profundo: Pacífico del Chocó. |
| P5 | `#ECE5D6` | Cierre seco: vuelve al papel desnudo. |

### 1.3 Tipografía (Google Fonts; pesos y px exactos)

- **Big Shoulders Display** (titulares, folio, cifras): mayúsculas, peso 700–900, condensado.
- **Petrona** (cuerpo, tesis, citas): serif; citas en itálica; peso 400–600.
- **Special Elite** (máquina de escribir): sellos, foliación pequeña, pies de imagen, etiquetas de expediente, referencias APA, franja de navegación. Solo piezas cortas (≤80 caracteres por línea).

**Reglas de jerarquía:**
- **Medida (line-measure) del cuerpo:** Petrona 400 a 26–30 px va a 55–65 ch máximo. Cita-testimonio Petrona italic 50–72 px va a 38–46 ch (cita más corta = más golpe).
- **Ratio de escala entre niveles consecutivos de la misma familia:** ≥1.3× en Petrona (cuerpo → cita), ≥1.4× en Big Shoulders (titular → palabra-grito → folio).
- **El testimonio manda.** Las citas textuales tienen tamaño mayor que la prosa del autor en cada panfleto donde aparecen.

Escala base (ajusta ±10% para encajar sin desbordar de forma fea):

| Elemento | Fuente | Peso | Tamaño px | Interlineado | Tracking |
|---|---|---|---|---|---|
| Folio (00–05) | Big Shoulders | 900 | altura mayúscula ≈ 300 | — | −2% |
| Palabra-grito (P0 línea 2, P5 línea 2) | Big Shoulders | 900 | 200–280 | 0.86 | −2% |
| Titular de panfleto | Big Shoulders | 800 | 110–180 | 0.9 | −1% |
| Bajada / itálica | Petrona italic | 500 | 32–38 | 1.3 | 0 |
| Cita-testimonio | Petrona italic | 500 | 50–72 | 1.12 | 0 |
| Cuerpo / tesis | Petrona | 400 (énfasis 600) | 26–30 | 1.45 | 0 |
| Sello | Special Elite | 400 | 28–40 | 1.05 | +6% |
| Pie de imagen / etiqueta | Special Elite | 400 | 20–24 | 1.3 | +5% |
| Franja navegación | Special Elite | 400 | 22 | — | +5% |

### 1.4 Texturas y "impresión" (obligatorio en los 6)

- **Grano de fotocopia** (capa superior global): ruido monocromo de frecuencia alta (equivalente SVG `feTurbulence baseFrequency=0.85 numOctaves=2`), tintado hacia tinta gastada `#574E40`, opacidad 10%, blend `multiply`. Cubre el lienzo entero.
- **Desregistro risográfico** (regla mecánica, no decorativa): cada elemento en rojo `#CC2F26` se duplica en una capa fantasma desplazada `(+3 px, +2 px)`, opacidad 75%, **debajo** del original. Cuando el elemento es papel sobre rojo (P0), el fantasma es tinta `#211C16` con el mismo desplazamiento.
- **Viñeteado** sutil: gradiente radial desde las cuatro esquinas hacia el centro, oscurecimiento 8% en las esquinas, transparente al 45% del radio. No saturar el centro.
- **Filetes:** reglas de 4–6 px en tinta `#211C16` como separadores principales; 2–3 px en tinta gastada para separadores secundarios. Sin radio, sin sombra. Nunca líneas de 1 px tímidas.
- **Bordes ásperos:** títulos, sellos y folios pierden 2–4% del trazo en mordidas aleatorias de 1–3 px (efecto linóleo / fotocopia mal tirada). No vectorial perfecto.
- **Sin sombras suaves, sin gradientes** salvo el viñeteado descrito arriba. Todo es tinta plana o papel plano.

### 1.5 Sello (construcción exacta)

- **Forma:** caja rectangular sin redondeo, **sin relleno** (deja ver el papel/fondo).
- **Borde:** 3 px del color del sello (rojo `#CC2F26` salvo que se indique tinta `#211C16`).
- **Padding interno:** 14 px arriba/abajo, 18 px izquierda/derecha.
- **Texto:** Special Elite 28–40 px, mayúsculas, tracking +6%, máximo 2 líneas.
- **Ancho resultante de la caja:** 220–360 px (se calcula a partir del texto + padding; no fijar arbitrariamente).
- **Rotación:** entre −6° y +6°. La rotación se varía entre sellos del mismo panfleto para no repetir el mismo gesto.
- **Erosión:** 10–20% del trazo del borde y del texto está ausente (tinta saltada). Si el sello es rojo, también aplica doble registro `(+3, +2 px)` como cualquier otro elemento rojo.
- **Separación mínima:** 80 px de cualquier borde del lienzo y 60 px de otro elemento tipográfico mayor.

### 1.6 Folio (esquina superior izquierda, los 6)

Número de 2 dígitos (`00`…`05`) en Big Shoulders 900, altura ≈ 300 px, color rojo `#CC2F26`, con **fantasma en tinta** desplazado −4,−3 px al 18% de opacidad. Esquina: x≈64, borde superior sangrando ligeramente fuera (y≈ −10 a 300). Es el elemento más grande tras el titular.

**Excepción P0:** en fondo rojo el folio va en papel `#ECE5D6` (no rojo), con fantasma en tinta.

### 1.7 Franja de navegación inferior (los 6, idéntica)

- Banda y∈[986,1050], fondo papel `#ECE5D6` (en P0 también papel, no rojo), separada del contenido por un **filete de 6 px en tinta** en y=986.
- Contenido en Special Elite 22 px, tinta, mayúsculas, tracking +5%:
  - Izquierda (x≈64): `← ANTERIOR` (en P0 atenuado al 28%, es el primero).
  - Centro: 6 puntos ⌀14 px, separación 28 px, borde tinta 2 px; el del panfleto actual **relleno rojo**. Estados: P0 `●○○○○○`, P1 `○●○○○○`, P2 `○○●○○○`, P3 `○○○●○○`, P4 `○○○○●○`, P5 `○○○○○●`.
  - Derecha (x≈1616, alineado a la derecha): `SIGUIENTE →` (en P5 cambia a `VOLVER AL INICIO ↺`).
  - Extremo derecho, más pequeño (18 px, tinta gastada): `PANFLETO 0X / 05`.

### 1.8 Prohibido (negative prompt)

**Prohibiciones absolutas (si aparece alguna, rechazar la imagen y rehacer):**
- Filetes de color como acento lateral decorativo (`border-left/right` >1 px en bloques de cita o callouts).
- Texto con gradiente (`background-clip: text` o equivalente). El énfasis va con peso, tamaño o color sólido.
- Glassmorphism, blur decorativo, cristal esmerilado.
- Plantilla SaaS *hero-metric*: gran cifra + etiqueta pequeña + acento en gradiente.
- Rejilla de tarjetas idénticas (icono + título + texto) repetidas.
- Modal o diálogo flotante simulado.

**Prohibido por brief específico:**
- Fotorrealismo de víctimas, sangre o de la masacre real (Bojayá, Las Delicias).
- Hero centrado tipo SaaS o landing.
- Estética de museo / comisión de la verdad pulcra y conciliadora.
- Apropiación folclórica decorativa de lo afro o lo campesino como "patrón bonito".
- *Edgy* decorativo gratuito (glitch de moda, sangre estética). La crudeza viene del documento, no del efecto.
- Brillo, emojis, banderas o colores fuera de la paleta de §1.2.
- Texto mal escrito, sin tildes, o con «comillas latinas» convertidas a `"`.
- Marcas de agua, firmas, logos de stock.

### 1.9 Ritmo y composición

- **Padding nunca uniforme.** El espacio vertical entre bloques varía deliberadamente: apretado 12–20 px (dentro de un mismo bloque), normal 40–56 px (entre bloques relacionados como cita + atribución), respiro 96–140 px (entre cabecera y cuerpo, o entre cuerpo y pie).
- **Composición asimétrica.** Nunca centrar el bloque principal. El folio crea un peso visual en la esquina sup. izq.; el resto contrabalancea hacia la derecha/abajo.
- **Sangrados deliberados.** Al menos un elemento por panfleto (titular grande o ilustración) se corta en un borde. El corte es intencional, no accidente.
- **Sin contenedor universal.** Nada lleva caja redondeada ni sombra suave alrededor. El papel ES la caja.

---

## 2. PANFLETO POR PANFLETO

> Coordenadas como guía de composición (no tienen que ser exactas al píxel, pero sí respetar zonas, jerarquía y proporciones). El **texto va literal, sin reescribir**.

---

### P0 — Portada: Pregunta Orientadora → `posters/p0.png`

**Concepto:** El cartel que abre el zine. No da respuesta: lanza la pregunta que estructurará todo lo que sigue. La pregunta ES la acusación.
**Fondo:** drench completo **rojo profundo `#9B241D`** con grano y viñeteado. Tipografía en papel `#ECE5D6`.

Composición (de arriba abajo):

1. **Crédito** — caja x[64,560] y[64,148]. Special Elite 24 px, papel, mayúsculas:
   `ANDRÉS SANABRIA · CÓDIGO 202113000` / `ELECTIVA «COLOMBIA»` / `EJE: MEMORIA Y VIOLENCIA · PROYECTO FINAL`
2. **Sello** — esquina sup. der., centro ≈ (1500,110), rotado +5°, borde papel 3 px, texto papel: `ENSAYO VISUAL`.
3. **Folio** `00` en papel `#ECE5D6` (excepción), x≈64, y≈ −10..300 (sangra arriba), fantasma tinta.
4. **Pregunta orientadora** — bloque y[260,820], tipografía papel, asimétrico sangrando a la izquierda desde x=52. Dividida en tres líneas de escala descendente para crear jerarquía tipográfica dentro de la pregunta:
   - Línea 1 (Big Shoulders 700, ≈90 px, opacidad 80%): `¿CÓMO SE MANIFIESTAN`
   - Línea 2 (Big Shoulders 900, ≈220 px, sangra por la derecha): `LAS RELACIONES DE PODER`
   - Línea 3 (Big Shoulders 800, ≈110 px, tracking +4%): `EN TORNO A MEMORIA Y VIOLENCIA,`
   - Línea 4 (Big Shoulders 700, ≈64 px, opacidad 70%): `A PARTIR DE LAS PERSPECTIVAS DE LAS FUENTES?`
   El fantasma de tinta corre ligeramente sobre las líneas 2 y 3 (las más grandes), efecto desregistro.
5. **Subetiqueta** — Special Elite 22 px, papel, y≈840: `Eje de indagación elegido: memoria y violencia.`
6. **Filete** papel 4 px, x[64,1616] y≈870.
7. **Índice de panfletos** — x[64,1616] y[884,980], Special Elite 24 px, papel; números en rojo con desregistro; separadores `·`:
   `01 TESIS · 02 COERCIÓN FÍSICA · 03 COERCIÓN ECONÓMICA · 04 COERCIÓN CULTURAL · 05 CONCLUSIÓN`
8. **Franja de navegación** (§1.7) estado `●○○○○○`, `← ANTERIOR` atenuado, derecha `SIGUIENTE →`, `PANFLETO 00 / 05`.

---

### P1 — Tesis y Referencias → `posters/p1.png`

**Concepto:** El manifiesto de postura. Antes de ver los casos, la audiencia lee la tesis completa y las fuentes que la sostienen. El rigor es visible.
**Fondo:** papel `#ECE5D6`; grano. Sin ilustración; póster textual.

Composición:

1. **Folio** `01` rojo gigante desregistrado, sup. izq. (x≈64, y −10..300).
2. **Titular** Big Shoulders tinta ≈150 px, a la derecha del folio: `TESIS`.
3. **Sello** rojo rotado +4°, centro ≈ (1460,180): `POSTURA SOSTENIDA`.
4. **Filete** tinta 6 px, x[64,1616] y≈330.
5. **Tesis completa** — x[64,1100] y[360,660], Petrona 400 30 px, tinta, interlineado 1.45, medida ≤65 ch. Texto **literal**:
   «Las relaciones de poder se manifiestan a través de la coerción física, económica y cultural de grupos poderosos —como los dueños del capital, altos mandos del ejército o grupos armados— sobre grupos vulnerables, como los protagonistas de las tres fuentes primarias.»
   Las palabras **física, económica y cultural** van en Petrona 600 (negrita dentro del bloque).
6. **Tres ejes** — columna x[1120,1616] y[360,660], Special Elite 20 px, tinta, cada línea con prefijo en rojo:
   `02  COERCIÓN FÍSICA` / `    Los cuerpos reclutados` (tinta gastada)
   `03  COERCIÓN ECONÓMICA` / `    La tierra robada` (tinta gastada)
   `04  COERCIÓN CULTURAL` / `    El canto que no calla` (tinta gastada)
   Separados por filetes delgados (2 px, tinta gastada) entre cada eje.
7. **Filete** tinta 4 px, x[64,1616] y≈680.
8. **Bloque de referencias** — x[64,1616] y[700,970], Special Elite 20 px, tinta gastada, dos columnas con gutter de 80 px (col. izq. x[64,810], col. der. x[890,1616]):

   Columna izquierda — encabezado Special Elite 22 px tinta: `FUENTES PRIMARIAS`; filete tinta 3 px debajo. Luego:
   `Hoyos Estrada, J. F. (1997). De Las Delicias al infierno: 288 días en poder de las FARC. Intermedio Editores.`
   `Ojeda, D., Guerra, P., Aguirre, C., & Díaz, H. (2016). Caminos condenados. Laguna Libros.`
   `Universidad ICESI. (2016). Voces de resistencia: Alabadoras de Pogue-Bojayá, Chocó [Video]. YouTube.`

   Columna derecha — encabezado Special Elite 22 px tinta: `FUENTES SECUNDARIAS`; filete tinta 3 px debajo. Luego:
   `Rodríguez Hernández, S. (2008). Colombia: ¿Morir por la patria? En De milicias reales militares contrainsurgentes (pp. 71–76). Javeriana.`
   `Ojeda, D., Petzl, J., Quiroga, C., Rodríguez, A. C., & Rojas, J. G. (2015). Paisajes del despojo cotidiano. Revista de Estudios Sociales, 54, 107–119.`
   `Quiceno, N., Ochoa Sierra, M., & Villamizar, A. (2017). La política del canto y el poder de las alabaoras de Pogue. Estudios Políticos, 51, 175–195.`

9. **Franja de navegación** estado `○●○○○○`, `PANFLETO 01 / 05`.

---

### P2 — Coerción física a través del cuerpo de los soldados → `posters/p2.png`

**Concepto:** El Estado selecciona por clase qué cuerpos son prescindibles. No es negligencia: es la lógica del poder.
**Fondo:** papel `#ECE5D6` con tinte frío muy sutil (hue ligeramente azulado); grano.

**Ilustración (linograbado / cartel agitprop a 2 tintas, negro `#211C16` + rojo `#CC2F26`; NO foto, NO documento):**
Ocupa la mitad inferior-izquierda, caja aprox x[40,920] y[430,1000], puede sangrar por abajo/izquierda. Escena:
- **Plano medio-largo en diagonal** que sube de abajo-izquierda hacia arriba-derecha: una **columna densa de jóvenes reclutas pobres** (10–14 figuras), siluetas macizas en negro, cabezas rapadas o con gorra de cuartel, morrales/petates al hombro, ropa humilde, todos de espalda o de perfil avanzando; las figuras se hacen más pequeñas hacia el fondo (perspectiva).
- Al final de la fila, arriba-derecha de la ilustración, la **reja/portón de un cuartel precario** de tablones en plena selva; sobre el portón un asta con bandera en tinta. Detrás, masas negras de selva (frondas dentadas) que aplanan la escena.
- En primer plano abajo-izquierda, separada por una reja, una **figura de élite** (silueta con saco, sentada a un escritorio) que entrega/recibe una **libreta roja**: representa a quien paga y no entra. Contraste de clase explícito.
- Tratamiento: alto contraste, masas negras planas (sin grises intermedios), **textura de gubia** (líneas talladas blancas/papel sobre los negros, peso 2–4 px, dirección variable, espaciado irregular), bordes erosionados, registro del rojo ligeramente corrido. Sin rostros detallados (siluetas), digno, no gore.
- **Cobertura de tinta negra en la caja de ilustración:** 55–70% del área. Resto papel. Sin grises, sin tramados de medio tono.
- **Carga de rojo:** ≤10% de la caja de ilustración (libreta militar + bandera del cuartel + acentos puntuales). El resto es tinta negra plana sobre papel.

**Texto (mitad superior y columna derecha):**
1. **Folio** `02` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈160 px, a la derecha del folio, 2 líneas: `COERCIÓN FÍSICA` / `LOS CUERPOS RECLUTADOS`.
3. **Bajada** Petrona itálica 36 px tinta gastada, bajo el titular:
   «El Estado envía a los más jóvenes y más pobres a morir. Los altos mandos los reducen a estadísticas.»
4. **Filete** tinta 6 px a todo el ancho, y≈370.
5. **Cita-testimonio dominante** — bloque x[920,1616] y[400,700], Petrona itálica 58 px, comilla roja ≈120 px desregistrada a la izquierda:
   «Los ricos ponen la plata y los pobres ponen los muertos.»
   Atribución Special Elite 22 px: `— RODRÍGUEZ HERNÁNDEZ, 2008, P. 73`.
6. **Cita de apoyo** — franja papel-mancha `#DCD3BD`, x[920,1616] y[720,900], Petrona 400 26 px tinta, interlínea 1.4:
   «Todos los soldados que pelearon y murieron en "Las Delicias" eran de origen humilde, quienes sólo trataban de cumplir con un deber estipulado legalmente para poder obtener un trabajo tras su licenciamiento.»
   Atribución Special Elite 20 px tinta gastada: `— RODRÍGUEZ HERNÁNDEZ, 2008, P. 73`.
7. **Sello** rojo rotado −5°, centro ≈ (1470,390): `CARNE DE CAÑÓN`.
8. **Nota de fuente** — Special Elite 20 px tinta gastada, x[64,1616] y[948,978]:
   `FUENTE PRIMARIA: HOYOS ESTRADA (1997) · CONTEXTO: RODRÍGUEZ HERNÁNDEZ (2008)`.
9. **Franja de navegación** estado `○○●○○○`, `PANFLETO 02 / 05`.

---

### P3 — Coerción económica a través del acaparamiento de tierras → `posters/p3.png`

**Concepto:** Tablero de evidencias del despojo cotidiano. La violencia no desapareció con la guerra: mutó y se volvió legal.
**Fondo:** papel `#ECE5D6` tinte terroso cálido; grano.

**Imágenes del cómic como referencia visual (NO insertar por código; observar y replicar con generación de imágenes):**

Antes de generar P3, abre y observa los 3 PNG de referencia:
- `/home/andy-spike/Documents/Uni/Colombia/public/img/comic/palma-carros.png`
- `/home/andy-spike/Documents/Uni/Colombia/public/img/comic/desplazamiento.png`
- `/home/andy-spike/Documents/Uni/Colombia/public/img/comic/campesina.png`

Luego replícalos en el cartel generado con el mismo estilo de la novela gráfica original (línea de cómic, blanco y negro, trazo de ilustración) pero integrados como **clippings recortados con tijera** (borde irregular de 2–6 px de variación, mordidas pequeñas), con un trozo de cinta y rotación leve. Tratamiento en blanco y negro de alto contraste para que peguen con la risografía: cobertura de tinta 45–60% de cada caja, sin grises intermedios.

**Cinta sobre cada clipping:** rectángulo de papel-mancha `#DCD3BD` al 70% de opacidad, ancho 70–110 px, alto 20–28 px, bordes irregulares (no rectángulo perfecto), colocada sobre una esquina o borde del clipping, con rotación independiente entre ±3° y ±8°. Una sola cinta por clipping; nunca dos.

| Escena a replicar | Caja destino aprox. | Rotación |
|---|---|---|
| palma-carros: casas campesinas con carros del agronegocio entrando entre palmeras | x[60,440] y[440,980] | −4° |
| desplazamiento: una mano que tacha el territorio; personas cargando lo que pueden y marchándose | x[450,950] y[400,940] | +3° |
| campesina: figura femenina resistiendo rodeada de palmas | x[1100,1620] y[490,1000] | +5° |

Pie Special Elite 20 px bajo cada recorte (tinta), con flecha roja `▸`:
- palma-carros → `Casas campesinas y carros del agronegocio entrando entre la palma.`
- desplazamiento → `Una mano tacha el territorio; la gente carga lo que puede y se va.`
- campesina → `Quien se queda resiste, rodeada de palma y de miedo.`

**Texto:**
1. **Folio** `03` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈160 px a la derecha del folio: `LA TIERRA ROBADA`.
3. **Bajada** Petrona itálica 36 px tinta gastada: «El despojo no terminó con la guerra: se volvió legal, lento y cotidiano.»
4. **Filete** tinta 6 px, y≈330.
5. **Cita-testimonio dominante** — franja de papel opaca cruzando el centro sobre los recortes, x[440,1110] y[530,780], Petrona itálica 52 px, comilla roja:
   «Después de la desmovilización paramilitar del 2007, pensamos que ya íbamos a poder vivir tranquilos [...] Pero entonces en el 2008 comienzan a llegar todos los empresarios [...] El tipo lo cogía, lo encerraba, le quitaba el acceso al agua, le quitaba el acceso al camino, le cercaba todo alrededor.»
   Atribución Special Elite 20 px: `— LÍDER CAMPESINO, OVEJAS, JUNIO 2013 (EN OJEDA ET AL., 2015, P. 107)`.
6. **Sello** rojo rotado +6°, centro ≈ (1460,355): `DESIERTO VERDE`.
7. **Etiqueta de expediente** Special Elite 20 px, esquina inf. izq. sobre el primer recorte:
   `FUENTE: CAMINOS CONDENADOS · OJEDA, GUERRA, AGUIRRE, DÍAZ · 2016`.
8. **Franja de navegación** estado `○○○●○○`, `PANFLETO 03 / 05`.

---

### P4 — Coerción cultural y el alabao como forma de resistencia → `posters/p4.png`

**Concepto:** La comunidad afectada convierte el duelo en denuncia política. La coerción no reprime la voz: la provoca.
**Fondo:** papel `#ECE5D6` tinte profundo muy sutil (más saturado, evocando el Chocó húmedo); grano.

**Ilustración (linograbado a 2 tintas, sobria y digna; NO caricaturesca; NO explotar el dolor):**
Caja aprox x[840,1660] y[280,1000], sangra por la derecha/abajo. Escena:
- **Tres a cinco mujeres afrocolombianas de pie, cantando** (las alabaoras de Pogue): siluetas negras macizas, **bocas abiertas en canto**, cabezas en alto, pañuelos/turbantes, vestidos largos; postura de fuerza colectiva, hombro con hombro, no de derrota.
- Detrás, el río Atrato y la selva del Chocó en masas negras simplificadas.
- Saliendo de las bocas, **ondas de sonido rojas `#CC2F26`** que viajan hacia la izquierda: 3–5 trazos curvos concéntricos por boca, peso decreciente 8 → 3 px, separación irregular (no paralelas perfectas). La onda más alejada cruza al menos 30% del ancho del lienzo (la voz que viaja lejos). Rojo desregistrado.
- Textura de gubia (peso 2–4 px, dirección variable), alto contraste, masas negras planas, bordes erosionados. Sin rostros detallados; gesto y postura, no sangre ni dolor explícito.
- **Cobertura de tinta negra en la caja de ilustración:** 50–65%. **Carga de rojo:** ondas de sonido, no más del 8% del área.

**Texto (mitad izquierda):**
1. **Folio** `04` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈140 px, 2 líneas: `EL CANTO` / `QUE NO CALLA`.
3. **Bajada** Petrona itálica 36 px tinta gastada: «Bojayá convirtió su duelo en acto político. La voz que honra a sus muertos también denuncia a quienes los causaron.»
4. **Filete** tinta 6 px, y≈360.
5. **Cita-testimonio dominante** — x[64,840] y[400,720], Petrona itálica 58 px, comilla roja. Esta cita es un **alabao** (verso): presentar con saltos de línea que respeten la métrica:
   «Nosotros los campesinos
   hemos sido maltratados,
   la pelea de los armados
   nosotros hemos pagado.»
   Atribución Special Elite 22 px: `— PALOMEQUE, 2014 (EN QUICENO ET AL., 2017, P. 189)`.
6. **Bloque de contexto** — x[64,840] y[740,920], Petrona 400 26 px tinta, interlínea 1.4:
   «Las alabaoras encontraron en el alabao una herramienta para conmemorar lo que la guerra les ha quitado, una forma de recordar más allá de la violencia. Han podido terminar en La Casa de Nariño transmitiendo su mensaje.»
7. **Sello** rojo rotado +3°, centro ≈ (580,940): `PROHIBIDO OLVIDAR`.
8. **Nota de fuente** — Special Elite 20 px tinta gastada, y≈952:
   `FUENTE: UNIVERSIDAD ICESI (2016) · CONTEXTO: QUICENO ET AL. (2017)`.
9. **Franja de navegación** estado `○○○○●○`, `PANFLETO 04 / 05`.

---

### P5 — Conclusión: diversidad de formas en que el Estado ejerce el poder → `posters/p5.png`

**Concepto:** Cierre desnudo y brutal. No consuela: interpela. El póster más tipográfico y despojado.
**Fondo:** papel `#ECE5D6`; grano; espacio negativo deliberado.

1. **Folio** `05` rojo gigante desregistrado, sup. izq.
2. **Titular** Big Shoulders tinta ≈150 px a la derecha del folio: `¿Y AHORA QUÉ?`.
3. **Filete** tinta 6 px, y≈330.
4. **Sentencia descomunal** — centro del lienzo, x[64,1616] y[360,700], Big Shoulders, 2 partes con ratio dramático 2.75×:
   - Línea 1, en tinta, peso 700, ≈80 px, tracking −1%: `EL PODER SE SOSTIENE`
   - Línea 2, debajo, en **rojo `#CC2F26`** peso 900, ≈220 px, tracking −2%, con fantasma tinta desregistrado `(+3, +2 px)`, sangrando 12–20 px por ambos lados: `A TRAVÉS DE LA VIOLENCIA.`
5. **Tres líneas de síntesis** — bloque x[64,900] y[720,880], Special Elite 22 px, tinta, cada línea con prefijo en rojo:
   `02 · FÍSICA: el Estado prescinde de los más pobres para sus objetivos militares.`
   `03 · ECONÓMICA: el capital usa las vías legales para continuar el despojo.`
   `04 · CULTURAL: la coerción no silenció la voz; la convirtió en denuncia.`
6. **Bloque de reflexión final** — x[920,1616] y[720,920], Petrona 400 26 px tinta, interlínea 1.4:
   «Estas historias demuestran que las decisiones de los grupos poderosos están desconectadas de la realidad de las regiones y manipulan activamente a las poblaciones para seguir operando: los nuevos terratenientes que prometen progreso, los reclutas que esperan refuerzos que nunca llegan. La violencia no desapareció: se transformó.»
7. **Sello** rojo grande rotado −3°, centro ≈ (1380,840): `NUNCA MÁS`.
8. **Expediente de fuentes** — Special Elite 20 px tinta gastada, x[64,1616] y[936,978]:
   `HOYOS ESTRADA 1997 · OJEDA ET AL. 2016 · UNIVERSIDAD ICESI 2016 · RODRÍGUEZ HERNÁNDEZ 2008 · OJEDA ET AL. 2015 · QUICENO ET AL. 2017`.
9. **Franja de navegación** estado `○○○○○●`; a la derecha `VOLVER AL INICIO ↺`; `PANFLETO 05 / 05`.

---

## 3. Prompts sugeridos por póster (si generas por texto→imagen)

Estilo común a anteponer en los 6:

> *Cartel político de pasquín fotocopiado, risografía a dos tintas, estética de taller de serigrafía latinoamericano y agitprop años 70-80, grano de fotocopia, registro de tinta roja ligeramente corrido, bordes erosionados, composición editorial asimétrica, tipografía condensada de manifestación, papel hueso #ECE5D6, tinta #211C16, rojo #CC2F26. Sin fotorrealismo, sin gradientes, sin brillo, sin glassmorphism, sin logos.*

- **P0:** *fondo rojo profundo #9B241D drench, gran pregunta tipográfica fragmentada en cuatro líneas de escala descendente "¿CÓMO SE MANIFIESTAN / LAS RELACIONES DE PODER / EN TORNO A MEMORIA Y VIOLENCIA, / A PARTIR DE LAS PERSPECTIVAS DE LAS FUENTES?" con la segunda línea descomunal cortándose en el borde, índice mecanografiado de los 4 panfletos, sello "ENSAYO VISUAL". Solo tipografía, sin ilustración.*
- **P1:** *póster tipográfico en papel, tesis académica como pieza central en Petrona, tres ejes numerados en columna derecha, bloque denso de referencias APA en Special Elite a dos columnas, sello "POSTURA SOSTENIDA", composición de expediente oficial.*
- **P2:** *linograbado a 2 tintas: columna diagonal de jóvenes reclutas pobres en silueta negra con petates marchando hacia la reja de un cuartel de tablones en la selva; en primer plano, separada por una reja, una figura de saco que paga una libreta roja; masas negras de selva al fondo; cita enorme "Los ricos ponen la plata y los pobres ponen los muertos" a la derecha, sello "CARNE DE CAÑÓN".*
- **P3:** *tablero de evidencias: collage de tres recortes de cómic en blanco y negro (se incrustan aparte) con cinta y rotación, gran cita testimonial de campesino de Ovejas sobre franja de papel cruzando el centro, sello "DESIERTO VERDE", etiqueta de expediente mecanografiada.*
- **P4:** *linograbado a 2 tintas, digno y sobrio: tres a cinco mujeres afrocolombianas de pie cantando en silueta negra, bocas abiertas, ondas de sonido rojas saliendo y viajando lejos; cita del alabao en verso a la izquierda; sin sangre, postura de fuerza colectiva, sello "PROHIBIDO OLVIDAR".*
- **P5:** *cartel tipográfico desnudo, mucho espacio en papel, sentencia descomunal "A TRAVÉS DE LA VIOLENCIA" en rojo enorme con fantasma de tinta corrido, tres líneas de síntesis en columna izquierda, párrafo de reflexión en serif a la derecha, sello "NUNCA MÁS".*

---

## 4. Checklist QA (por póster, antes de entregar)

- [ ] 1680×1050 px exactos. Solo la paleta de §1.2 (incluido el tinte de fondo correcto por panfleto).
- [ ] Folio gigante rojo desregistrado sup. izq.; franja de navegación inferior con **6 puntos** y el punto correcto relleno, textos de §1.7.
- [ ] Titular en Big Shoulders, cuerpo/cita en Petrona, etiquetas/sellos en Special Elite. Ratios de escala según §1.3 (≥1.3× Petrona, ≥1.4× Big Shoulders).
- [ ] Medida del cuerpo dentro de 55–65 ch; cita-testimonio en 38–46 ch.
- [ ] Copy **literal del ensayo**, con tildes y «comillas latinas» correctas; sin texto inventado, sin abreviaciones, sin recortar a media palabra.
- [ ] Grano `feTurbulence` 0.85/2 al 10% multiply; desregistro rojo `(+3, +2 px)` al 75%; filetes de 4–6 px; sellos rotados con tinta saltada y separación mínima de 80 px del borde.
- [ ] Sin gradientes (excepto viñeteado), sin sombras suaves, sin glassmorphism, sin filetes de color como acento lateral, sin texto con gradiente, sin plantilla *hero-metric*, sin rejilla de tarjetas (§1.8).
- [ ] P0 fondo rojo profundo, solo tipografía; P1 bloque de referencias completo con gutter de 80 px; P5 tipográfico con espacio negativo y ratio 2.75× entre líneas.
- [ ] P2 y P4 con ilustración linograbado original (cobertura tinta 50–70%, gubia 2–4 px, sin grises, sin gore).
- [ ] P3 reproduce las 3 escenas del cómic mediante generación de imágenes (NO inserción por código), con estilo cómic B/N alto contraste, borde de recorte irregular, cinta `#DCD3BD` translúcida y su pie.
- [ ] Composición asimétrica, sangrados intencionales (al menos uno por panfleto), padding no uniforme (§1.9).
- [ ] Reporte final: método exacto, archivos + dimensiones, desviaciones/limitaciones.
