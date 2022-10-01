import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import * as path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    manifest: true,
    outDir: path.resolve(__dirname, "../static/"),
    rollupOptions: {
      input: 'src/main.js',
      output: {
        entryFileNames: "[name].js",
        assetFileNames: "[name][extname]"
      },
    }
  },
  server: {
    host: '0.0.0.0'
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
