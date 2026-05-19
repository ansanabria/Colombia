import { defineConfig } from 'astro/config';

// Sitio estático. El zine se entrega como /dist servible o doble clic vía preview.
export default defineConfig({
  site: 'https://zine-memoria.local',
  trailingSlash: 'always',
  build: { format: 'directory' },
  devToolbar: { enabled: false },
});
