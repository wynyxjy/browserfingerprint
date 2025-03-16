function hashStr(s) {
  var hash = 0
  if (s.length == 0) return hash
  for (i = 0; i < s.length; i++) {
    char = s.charCodeAt(i)
    hash = (hash << 5) - hash + char
    hash = hash & hash
  }
  return hash
}
