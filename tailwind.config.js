const plugin = require('tailwindcss/plugin');

module.exports = {
  content: ['./app/*.html'],
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536px',
    },
    fontFamily: {
      sans: ['Mulish', 'sans-serif'],
      black: ['Mulish-Black', 'sans-serif'],
    },
    colors: {
      'header-bg': '#1F1254',
      heading: '#7768BF',
      'general-heading': '#13C0D1',
      placeholder: '#9498AB',
      nav: '#FFFFFF',
      'filter-name': '#090632',
      pagination: '#9498AB',
      'paginatoin-active': '#FFFFFF',
      'pagination-active-bg': '#13C0D1',
      'select-border': '#939498',
      'input-border': '#939498',
      text: '#1F1254',
      'filter-block-bg': '#FAF9FE',
      'button-bg': '#9484E3',
      'button-text': '#FFFFFF',
      'table-head': '#FAF9FE',
      'text-table-head': '#7768BF',
      'border-table': 'rgba(18, 24, 55, 0.16)',
      'pagination-hover': '#F0F1F4',
      appearance: '#090632',
      'text-disable': '#9498AB',
    },

    container: {
      padding: {
        DEFAULT: '1rem',
      },
      center: true,
    },
    extend: {},
  },
  plugins: [
    plugin(function ({ addBase }) {
      addBase({
        '@font-face': {
          fontFamily: 'Mulish',
          src: 'url(/fonts/Mulish-VariableFont_wght.ttf)',
        },
        '@font-face': {
          fontFamily: 'Mulish-Black',
          src: 'url(/fonts/Mulish-Black.ttf)',
        },
      });
    }),
  ],
};
``;
