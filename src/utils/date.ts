export function formatDate(date: Date, format: 'iso' | 'long' | 'year' = 'iso'): string {
  switch (format) {
    case 'year':
      return new Intl.DateTimeFormat('en', { year: 'numeric' }).format(date)
    case 'long':
      return new Intl.DateTimeFormat('en', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      }).format(date)
    case 'iso':
    default:
      return date.toISOString().split('T')[0]
  }
}
