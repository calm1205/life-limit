export function calculateDays(year, month, day) {
  const birthDate = new Date(year, month - 1, day)
  const today = new Date()

  const diffTime = Math.abs(today - birthDate)
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))

  return diffDays
}
