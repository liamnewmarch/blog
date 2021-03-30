/**
 * Controls the site theme! If the browser supports color scheme media queries
 * then the default theme will auto-switch between light and dark depending
 * on OS settings, otherwise a dark theme will be used. If the user changes
 * theme this will be saved in local storage for their next visit.
 *
 * @typedef {{ icon: string, name: string }} Theme
 */
export class ThemeController {
  /**
   * A basic check for color scheme media query support.
   * @return {boolean}
   */
  static getMediaQuerySupport() {
    if (!window.matchMedia) return false;
    return window.matchMedia('(prefers-color-scheme)').matches;
  }

  /**
   * Get themes depending on browser support. Browsers that support color
   * scheme media queries get an 'auto' setting
   * @yield {Theme}
   */
  static* getSupportedThemes() {
    if (this.getMediaQuerySupport()) {
      // Auto theme - the default if supported.
      yield {
        icon: 'brightness_auto',
        name: 'auto',
      };
    }

    // Dark theme - the default if auto is not supported.
    yield {
      icon: 'brightness_3',
      name: 'dark',
    };

    // Light theme
    yield {
      icon: 'brightness_7',
      name: 'light',
    };
  }

  /**
   * Returns an infinite interator for looping over themes indefinitely.
   * @param {Theme[]} themes Themes to cycle through.
   * @param {Theme} theme Theme to start with.
   */
  static* themeIterator(themes, theme) {
    let i = themes.findIndex(({ name }) => name === theme.name) || 0;
    while (true) {
      i = (i + 1) % themes.length;
      yield themes[i];
    }
  }

  /**
   * Gets the stored theme if there is one, or returns the default theme.
   * @return {Theme}
   */
  get theme() {
    const theme = localStorage.getItem('theme');
    return this.themes.find(({ name }) => name === theme) || this.themes[0];
  }

  /**
   * Saves the given theme in local storage for later retrieval
   * @param {Theme} theme
   */
  set theme(theme) {
    const event = new CustomEvent('toggle-theme', { detail: { ...theme }});
    if (theme.name === 'auto' && ThemeController.getMediaQuerySupport()) {
      event.detail.name = this.mediaQuery.matches ? 'light' : 'dark';
    }
    document.dispatchEvent(event);
    localStorage.setItem('theme', theme.name);
  }

  /**
   * Initialise themes, add listeners for the media query and local storage
   */
  constructor() {
    /** @type {Theme[]} */
    this.themes = [...ThemeController.getSupportedThemes()];

    /** @type {IterableIterator} */
    this.iterator = ThemeController.themeIterator(this.themes, this.theme);

    if (ThemeController.getMediaQuerySupport()) {
      /** @type {MediaQueryList=} */
      this.mediaQuery = window.matchMedia('(prefers-color-scheme: light)');
      this.mediaQuery.addListener(() => this.reset());
    }

    window.addEventListener('storage', () => this.reset());
  }

  /**
   * Syncs the themes iterator with the value in storage.
   * @param {number=} retry
   */
  reset(retry = this.themes.length) {
    if (!retry) throw new Error('Error resetting theme, couldn’t reset index');
    const theme = this.theme;
    const next = this.iterator.next().value;
    if (next === theme) {
      this.theme = next;
    } else {
      this.reset(retry--);
    }
  }

  /**
   * Get the next theme from the theme iterator.
   */
  toggle() {
    this.theme = this.iterator.next().value;
  }
}
