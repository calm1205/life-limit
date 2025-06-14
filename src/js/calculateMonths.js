export function calculateMonths(year, month, day) {
  const birthDate = new Date(year, month - 1, day)
  const today = new Date()

  const years = today.getFullYear() - birthDate.getFullYear()
  const months = today.getMonth() - birthDate.getMonth()

  return years * 12 + months
}
