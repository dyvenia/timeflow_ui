module.exports = {
  content: ['./app/*.html'],
  theme: {
    screens: {
      sm: '540px',
      md: '720px',
      lg: '960px',
      xl: '1140px',
      '2xl': '1140px',
    },
    fontFamily: {},
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
    },

    container: {
      padding: {
        DEFAULT: '1rem',
      },
    },
    extend: {},
  },
  plugins: [],
};
