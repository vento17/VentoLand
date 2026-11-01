import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://ventoland.it',
  trailingSlash: 'never',
  build: { format: 'file' },
});
