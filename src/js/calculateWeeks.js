export function calculateWeeks(year, month, day) {
  const birthDate = new Date(year, month - 1, day)
  const today = new Date()

  const diffTime = Math.abs(today - birthDate)
  const diffWeeks = Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 7))

  return diffWeeks
}
