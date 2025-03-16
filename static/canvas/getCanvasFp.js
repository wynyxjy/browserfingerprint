function getCanvasFp() {
  var result = ''
  var result1 = ''
  var result2 = ''
  var result3 = ''
  var result4 = ''
  var result5 = ''
  var result6 = ''

  if(document.getElementById('canvas')){
    var canvas = document.getElementById('canvas')
  }
  else{
    var canvas = document.createElement('canvas')
  }

  canvas.width = 400
  canvas.height = 20
  var ctx = canvas.getContext('2d')
  ctx.rect(0, 0, 10, 10)
  ctx.rect(2, 2, 6, 6)
  // isPointInPath 判断给定的坐标是否位于路径之内
  // evenodd fill方法 奇偶原则
  result +=
    'canvas winding:' +
    (ctx.isPointInPath(5, 5, 'evenodd') === false ? 'yes' : 'no')

  // 绘制边线
  ctx.textBaseline = 'alphabetic'
  ctx.fillStyle = '#f60'
  ctx.fillRect(125, 1, 62, 20)
  ctx.fillStyle = '#069'
  ctx.font = '11pt no-real-font-123'
  ctx.fillText('Cwm fjordbank glyphs vext quiz', 2, 15)
  ctx.fillStyle = 'rgba(102, 204, 0, 0.2)'

  // 绘制文字
  if(document.getElementById('canvas1')){
    var canvas1 = document.getElementById('canvas1')
  }
  else{
    var canvas1 = document.createElement('canvas')
  }
  canvas1.width = 400
  canvas1.height = 100
  var ctx1 = canvas1.getContext('2d')
  result1 +=
    'canvas1 winding:' +
    (ctx1.isPointInPath(5, 5, 'evenodd') === false ? 'yes' : 'no')
  ctx1.font = '18pt Arial'
  ctx1.fillText('Cwm fjordbank glyphs vext quiz', 4, 30)
  ctx1.font = '20px Arial'
  ctx1.fillText('Cwm fjordbank glyphs vext quiz', 4, 60)

  // 无意义文本
  if(document.getElementById('canvas')){
    var canvas2 = document.getElementById('canvas2')
  }
  else{
    var canvas2 = document.createElement('canvas')
  }
  canvas2.width = 400
  canvas2.height = 50
  var ctx2 = canvas2.getContext('2d')
  result2 +=
    'canvas2 winding:' +
    (ctx2.isPointInPath(5, 5, 'evenodd') === false ? 'yes' : 'no')
  ctx2.font = 'not even a font spec in the slightest'
  ctx2.fillText('Cwm fjordbank glyphs vext quiz', 4, 30)

  // 网络字体
  if(document.getElementById('canvas3')){
    var canvas3 = document.getElementById('canvas3')
  }
  else{
    var canvas3 = document.createElement('canvas')
  }
  canvas3.width = 400
  canvas3.height = 100
  var ctx3 = canvas3.getContext('2d')
  result3 +=
    'canvas3 winding:' +
    (ctx3.isPointInPath(5, 5, 'evenodd') === false ? 'yes' : 'no')
  ctx3.font = '12pt dsad'
  ctx3.fillText('Cwm fjordbank glyphs vext quiz', 4, 30)
  ctx3.font = '15px dsad'
  ctx3.fillText('Cwm fjordbank glyphs vext quiz', 4, 60)

  // emoji
  if(document.getElementById('canvas4')){
    var canvas4 = document.getElementById('canvas4')
  }
  else{
    var canvas4 = document.createElement('canvas')
  }
  canvas4.width = 400
  canvas4.height = 50
  var ctx4 = canvas4.getContext('2d')
  result4 +=
    'canvas4 winding:' +
    (ctx4.isPointInPath(5, 5, 'evenodd') === false ? 'yes' : 'no')
  ctx4.font = '20px Arial'
  ctx4.fillText('\ud83d\ude03', 4, 30)

  // webgl
  // var canvas5 = document.getElementById('canvas5')
  // canvas5.width = 2000
  // canvas5.height = 200
  // var ctx5 = canvas5.getContext('webgl')
  // if (ctx5 === null) {
  //   alert(
  //     'Unable to initialize WebGL. Your browser or machine may not support it.',
  //   )
  //   return
  // }

  // 绘制圆形
  if(document.getElementById('canvas6')){
    var canvas6 = document.getElementById('canvas6')
  }
  else{
    var canvas6 = document.createElement('canvas')
  }
  canvas6.width = 400
  canvas6.height = 150
  // canvas1.style.display = 'inline'
  var ctx6 = canvas6.getContext('2d')
  result6 +=
    'canvas6 winding:' +
    (ctx6.isPointInPath(5, 5, 'evenodd') === false ? 'yes' : 'no')
  ctx6.globalCompositeOperation = 'multiply'
  ctx6.fillStyle = 'rgb(255,0,255)'
  ctx6.beginPath()
  ctx6.arc(50, 50, 50, 0, Math.PI * 2, true)
  ctx6.closePath()
  ctx6.fill()
  ctx6.fillStyle = 'rgb(0,255,255)'
  ctx6.beginPath()
  ctx6.arc(100, 50, 50, 0, Math.PI * 2, true)
  ctx6.closePath()
  ctx6.fill()
  ctx6.fillStyle = 'rgb(255,255,0)'
  ctx6.beginPath()
  ctx6.arc(75, 100, 50, 0, Math.PI * 2, true)
  ctx6.closePath()
  ctx6.fill()
  ctx6.fillStyle = 'rgb(255,0,255)'
  ctx6.arc(75, 75, 75, 0, Math.PI * 2, true)
  ctx6.arc(75, 75, 25, 0, Math.PI * 2, true)
  ctx6.fill('evenodd')

  let resultAll = []

  if (canvas.toDataURL) {
    result += ';canvas fp:' + canvas.toDataURL()
    resultAll.push(result)
  }
  if (canvas1.toDataURL) {
    result1 += ';canvas1 fp:' + canvas1.toDataURL()
    resultAll.push(result1)
  }
  if (canvas2.toDataURL) {
    result2 += ';canvas2 fp:' + canvas2.toDataURL()
    resultAll.push(result2)
  }
  if (canvas3.toDataURL) {
    result3 += ';canvas3 fp:' + canvas3.toDataURL()
    resultAll.push(result3)
  }
  if (canvas4.toDataURL) {
    result4 += ';canvas4 fp:' + canvas4.toDataURL()
    resultAll.push(result4)
  }
  // if (canvas5.toDataURL) {
  //   result5 += ';canvas5 fp:' + canvas5.toDataURL()
  //   resultAll.push(result5)
  // }
  if (canvas6.toDataURL) {
    result6 += ';canvas6 fp:' + canvas6.toDataURL()
    resultAll.push(result6)
  }
  return resultAll
}
