import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "../static/frontend", // output goes into Django static folder
    emptyOutDir: true,
  },
});
