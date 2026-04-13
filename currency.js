(function(){
  var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
  var lang = navigator.language || '';
  var symbol = '\u20ac';
  var progress = '9.99';
  var premium = '14.99';
  var calcSymbol = '\u20ac';

  if (tz.indexOf('London') > -1 || tz.indexOf('Dublin') > -1 || lang.indexOf('en-GB') > -1) {
    symbol = '\u00a3'; progress = '8.99'; premium = '16.99'; calcSymbol = '\u00a3';
  } else if (tz.indexOf('America') > -1 || tz.indexOf('Pacific') > -1 || tz.indexOf('Eastern') > -1 || lang.indexOf('en-US') > -1) {
    symbol = '$'; progress = '10.99'; premium = '19.99'; calcSymbol = '$';
  } else if (tz.indexOf('Australia') > -1 || lang.indexOf('en-AU') > -1) {
    symbol = 'A$'; progress = '15.99'; premium = '29.99'; calcSymbol = 'A$';
  } else if (tz.indexOf('Canada') > -1 || lang.indexOf('en-CA') > -1) {
    symbol = 'C$'; progress = '14.99'; premium = '26.99'; calcSymbol = 'C$';
  }

  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.price-progress').forEach(function(el){ el.textContent = symbol + progress; });
    document.querySelectorAll('.price-premium').forEach(function(el){ el.textContent = symbol + premium; });
    document.querySelectorAll('.calc-currency').forEach(function(el){ el.textContent = calcSymbol; });
  });
})();
