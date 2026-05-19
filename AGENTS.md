# Notas para Agentes

## Idioma de trabajo

Todas las interacciones futuras con agentes deben realizarse en **español**.

---

## Contexto del Proyecto

Este proyecto corresponde a la clase electiva **"Colombia"** de la universidad, orientada a aprender temas generales sobre Colombia. La clase se dicta en español y este es el **proyecto final**.

### Instrucciones del proyecto final

En la unidad 3 (tres semanas y media), los estudiantes llevarán a cabo un trabajo de indagación grupal autónomo. Para ello se espera que, con orientación del profesor/a, pongan en práctica las habilidades y conocimientos desarrollados en las primeras dos unidades del curso.

Este trabajo autónomo invita a los estudiantes a indagar sobre un tema de su interés entre los que se ofrecen en la unidad. Los estudiantes analizarán y contextualizarán las fuentes del eje de indagación que elijan, y plantearán una tesis que dé respuesta a una pregunta de indagación. Este trabajo de indagación será presentado a sus compañeros de curso a través de algún medio de su elección (video, podcast, blog, entre otros).

El **eje temático** del proyecto de investigación es: **"Memoria y Violencia"**.

### Formato de entrega elegido

La entrega será una **página web narrativa y artística**, que funcione como un **ensayo visual** sobre la explotación de las minorías en Colombia.

**Estilo visual elegido:** Zine digital / colección de panfletos políticos-activistas. Navegación por capítulos (panfletos). Tono político/activista, crudo, con tipografía de manifestación, collages, y estética de fotocopia.

**Estructura propuesta del ensayo (5 panfletos):**

| Panfleto | Título | Contenido |
|----------|--------|-----------|
| **0** | *Portada / Manifiesto* | Título del proyecto, tesis en una frase contundente, lista de contenidos. |
| **1** | *Los cuerpos reclutados* | Conscripción obligatoria + ataque de Las Delicias. ¿Cómo el Estado utiliza los cuerpos de los jóvenes (especialmente de las clases populares) como carne de cañón? |
| **2** | *La tierra robada* | Despojo en Montes de María + novela gráfica *Caminos Condenados*. El agronegocio, el paramilitarismo y la transformación del territorio en "desierto verde". |
| **3** | *El canto que no calla* | Masacre de Bojayá (2002) y las *Musas de Pogue*. Cómo el alabao pasó de ser un ritual fúnebre a un acto político de memoria y exigencia de paz. |
| **4** | *¿Y ahora qué?* | Conclusión: conexiones entre los tres ejes. Memoria como acción política, no como nostalgia. Llamado a la acción o reflexión final. |

---

## Fuentes de investigación

Se deben trabajar **tres fuentes de investigación**. Cada fuente está compuesta por un **texto primario** y un **texto de contextualización**.

### Fuente 1: Los cuerpos reclutados
- **Texto primario:** `legacy/primaria-1.pdf` — *"Un ataque en Las Delicias"* (ataque militar en Putumayo).
  - **Formato:** PDF escaneado (7 páginas). **No tiene texto extraíble.**
  - **Acceso:** Imágenes renderizadas en `fuentes-imagenes/primaria-1-las-delicias/pagina-NN.png` e índice en `fuentes-transcritas/primaria-1-imagenes.md`.
- **Texto de contextualización:** `legacy/contexto-1.pdf` — *"¡Aquí comienza la excelencia!"* (conscripción y democracia en Colombia, por Saúl Rodríguez Hernández).
  - **Formato:** PDF escaneado (20 páginas). **No tiene texto extraíble.**
  - **Acceso:** Imágenes renderizadas en `fuentes-imagenes/contexto-1-conscripcion/pagina-NN.png` e índice en `fuentes-transcritas/contexto-1-imagenes.md`.

### Fuente 2: La tierra robada
- **Texto primario:** `legacy/primaria-2.pdf` — *"Caminos Condenados"* (novela gráfica sobre Montes de María, por Ojeda, Guerra, Aguirre, Díaz).
  - **Formato:** PDF con 48 páginas escaneadas de un libro físico. Es una novela gráfica.
  - **Acceso:** Páginas extraídas como imágenes PNG recortadas en `comic-paginas/caminos-condenados-NN.png` e índice en `fuentes-transcritas/primaria-2-comic.md`.
  - **Nota:** Las imágenes han sido recortadas automáticamente para eliminar márgenes en blanco del escáner, pero aún pueden tener bordes de libro/gutter. El próximo agente puede recortar paneles individuales si es necesario para el diseño web.
- **Texto de contextualización:** `legacy/contexto-2.pdf` — *"Paisajes del despojo cotidiano: acaparamiento de tierra y agua en Montes de María, Colombia"* (por Diana Ojeda et al., Revista de Estudios Sociales, 2015).
  - **Formato:** PDF nativo con texto extraíble (16 páginas).
  - **Acceso:** Texto transcrito a `fuentes-transcritas/contexto-2-paisajes-del-despojo-cotidiano.md`.

### Fuente 3: El canto que no calla
- **Texto primario:** [Video de YouTube](https://www.youtube.com/watch?v=2pKUJYzaWcQ) — miembros de la comunidad de Bojayá hablando de su experiencia con los alabaos.
  - **Nota:** mayoritariamente es más relevante el texto de contextualización que la misma fuente primaria.
- **Texto de contextualización:** `legacy/contexto-3.pdf` — *"La política del canto y el poder de las alabaoras de Pogue (Bojayá, Chocó)"* (por Natalia Quiceno Toro, María Ochoa Sierra, Adriana Marcela Villamizar, Estudios Políticos, 2017).
  - **Formato:** PDF nativo con texto extraíble (21 páginas).
  - **Acceso:** Texto transcrito a `fuentes-transcritas/contexto-3-alabaoras-de-pogue.md`.

---

## Estructura de directorios

```
/home/andy-spike/Documents/Uni/Colombia/
├── AGENTS.md                              # Este archivo
├── .venv/                                 # Entorno virtual Python (PDF)
├── scripts/
│   └── process_sources.py                 # Script usado para procesar las fuentes
├── legacy/                                # PDFs originales (no tocar)
│   ├── primaria-1.pdf
│   ├── primaria-2.pdf
│   ├── contexto-1.pdf
│   ├── contexto-2.pdf
│   └── contexto-3.pdf
├── fuentes-transcritas/                   # Texto extraído / índices de imágenes
│   ├── primaria-1-imagenes.md             # Índice de imágenes del texto primario 1
│   ├── primaria-2-comic.md                # Índice de imágenes del cómic
│   ├── contexto-1-imagenes.md             # Índice de imágenes del contexto 1
│   ├── contexto-2-paisajes-del-despojo-cotidiano.md  # Texto transcrito
│   └── contexto-3-alabaoras-de-pogue.md              # Texto transcrito
├── fuentes-imagenes/                      # Páginas de PDFs escaneados como PNG
│   ├── primaria-1-las-delicias/
│   │   └── pagina-01.png ... pagina-07.png
│   └── contexto-1-conscripcion/
│       └── pagina-01.png ... pagina-20.png
└── comic-paginas/                         # Páginas del cómic recortadas como PNG
    └── caminos-condenados-01.png ... caminos-condenados-48.png
```

---

## Entorno del skill PDF

El proyecto cuenta con un entorno virtual dedicado para los paquetes Python relacionados con PDF.

- **Ruta del venv**: `/home/andy-spike/Documents/Uni/Colombia/.venv`
- **Paquetes instalados**: `reportlab`, `pdfplumber`, `pypdf`, `pypdfium2`, `pillow`

Antes de ejecutar cualquier operación del skill `pdf`, activa el entorno o úsalo explícitamente:

```bash
# Opción 1: activar y ejecutar
source /home/andy-spike/Documents/Uni/Colombia/.venv/bin/activate
python3 <tu_script.py>

# Opción 2: invocar el Python del venv directamente
/home/andy-spike/Documents/Uni/Colombia/.venv/bin/python <tu_script.py>

# Opción 3: usar uv con el entorno
uv run -p /home/andy-spike/Documents/Uni/Colombia/.venv/bin/python <tu_script.py>
```

La herramienta del sistema `pdftoppm` (Poppler) ya está disponible globalmente.

---

## Estado actual del proyecto

- [x] Fuentes organizadas y procesadas
- [x] Textos extraíbles transcritos a Markdown
- [x] PDFs escaneados renderizados como imágenes PNG
- [x] Cómic extraído como imágenes PNG recortadas
- [x] PDFs originales archivados en `legacy/`
- [ ] Escribir el ensayo (contenido textual)
- [ ] Diseñar y construir la página web (HTML/CSS/JS)
- [ ] Buscar/curar imágenes adicionales de archivo
- [ ] Integrar todo en el zine digital

**Próximo paso sugerido:** Empezar por la Fase 1 (escribir el ensayo) o la Fase 2 (maquetar la estructura base del zine). La decisión depende de si el usuario quiere primero el contenido o la estructura visual.
