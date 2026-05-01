customElements.define('current-year', class extends HTMLElement {
  connectedCallback() {
    this.append(' ', new Intl.DateTimeFormat('en', {
      year: 'numeric',
    }).format(), ' ')
  }
})
