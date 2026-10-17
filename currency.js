// Afterbetting rekent af in euro. Alleen het valutateken in de rekenhulp volgt de bezoeker.
(function(){
  var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
  var lang = navigator.language || '';
  var calcSymbol = '\u20ac';
  if (tz.indexOf('London') > -1 || tz.indexOf('Dublin') > -1 || lang.indexOf('en-GB') > -1) calcSymbol = '\u00a3';
  else if (tz.indexOf('America') > -1 || lang.indexOf('en-US') > -1) calcSymbol = '$';
  else if (tz.indexOf('Australia') > -1 || lang.indexOf('en-AU') > -1) calcSymbol = 'A$';
  else if (tz.indexOf('Canada') > -1 || lang.indexOf('en-CA') > -1) calcSymbol = 'C$';
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.calc-currency').forEach(function(el){ el.textContent = calcSymbol; });
    window.ABCUR = calcSymbol;
    if (typeof window.updateCalc === 'function') window.updateCalc();
  });
})();
