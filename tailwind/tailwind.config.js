/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../app/**/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        heading: ["Epilogue", "sans-serif"],
      },
    },
  },
  plugins: [],
}

