export function calculateAge(year, month, day) {
  const birthDate = new Date(year, month - 1, day)
  const today = new Date()

  let age = today.getFullYear() - birthDate.getFullYear()
  const monthDiff = today.getMonth() - birthDate.getMonth()

  if (
    monthDiff < 0 ||
    (monthDiff === 0 && today.getDate() < birthDate.getDate())
  ) {
    age--
  }

  return age
}

export function getBirthParams() {
  const urlParams = new URLSearchParams(window.location.search)
  const year = parseInt(urlParams.get("year"))
  const month = parseInt(urlParams.get("month"))
  const day = parseInt(urlParams.get("day"))

  return { year, month, day }
}
