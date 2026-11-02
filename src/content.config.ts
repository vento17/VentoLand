import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Prodotti: un file .md per prodotto in src/content/prodotti/
const prodotti = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/prodotti' }),
  schema: z.object({
    nome: z.string(),
    tagline: z.string(),
    tipo: z.enum(['software', 'firmware', 'hardware']),
    stato: z.enum(['disponibile', 'beta', 'in-arrivo']).default('in-arrivo'),
    prezzo: z.string().optional(),          // es. "49 €" oppure "gratis"
    buy_url: z.string().url().optional(),   // link checkout Lemon Squeezy
    docs_url: z.string().optional(),
    repo_url: z.string().url().optional(),
    piattaforme: z.array(z.string()).default([]),
    immagine: z.string().optional(),        // es. /img/maestrale.jpg
    logo: z.string().optional(),            // es. /logo/prodotti/ventonet.png
    tags: z.array(z.string()).default([]),  // es. [free, opensource, esp32]
    ordine: z.number().default(99),
  }),
});

// Sul campo: un file .md per spettacolo/lavoro in src/content/campo/
const campo = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/campo' }),
  schema: z.object({
    titolo: z.string(),
    data: z.coerce.date(),
    luogo: z.string().optional(),
    ruolo: z.string().optional(),            // es. "Lighting designer e operatore"
    prodotti: z.array(z.string()).default([]), // slug dei prodotti usati
    copertina: z.string().optional(),
    video: z.string().url().optional(),      // YouTube / Vimeo
    galleria: z.array(z.string()).default([]),
  }),
});

// Docs: markdown libero in src/content/docs/<prodotto>/<pagina>.md
const docs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/docs' }),
  schema: z.object({
    titolo: z.string(),
    prodotto: z.string().optional(),
    ordine: z.number().default(99),
  }),
});

export const collections = { prodotti, campo, docs };
