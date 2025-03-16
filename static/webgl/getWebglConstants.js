// webglConstants
function getWebglConstants() {
  if(document.getElementById('webgl')){
    var webgl = document.getElementById('webgl')
  }
  else{
    var webgl = document.createElement('canvas')
  }
  webgl.width = 2000
  webgl.height = 200
  var ctx5 = webgl.getContext('webgl')
  if (ctx5 === null) {
    alert('Unable to initialize WebGL. Your browser or machine may not support it.')
    return
  }
  var vertexPosBuffer = ctx5.createBuffer();
  let resultWebgl = []
  var debugInfo = ctx5.getExtension('WEBGL_debug_renderer_info')
  // Debug Renderer Info ：
  // 供应商
  var vendor = ctx5.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL) === undefined ? '不支持该属性' : ctx5.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL)
  resultWebgl.push(vendor)
  // 渲染器
  var renderer = ctx5.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) === undefined ? '不支持该属性' : ctx5.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL)
  resultWebgl.push(renderer)
  console.log(vendor)
  console.log(renderer)

  // WebGL Context Info ：
  // Version
  var version = ctx5.getParameter(ctx5.VERSION) === undefined ? '不支持该属性' : ctx5.getParameter(ctx5.VERSION)
  resultWebgl.push(version)
  console.log('VERSION = ' + ctx5.getParameter(ctx5.VERSION))
  // SHADING_LANGUAGE_VERSION
  var SHADING_LANGUAGE_VERSION = ctx5.getParameter(ctx5.SHADING_LANGUAGE_VERSION) === undefined ? '不支持该属性' : ctx5.getParameter(ctx5.SHADING_LANGUAGE_VERSION)
  resultWebgl.push(SHADING_LANGUAGE_VERSION)
  console.log('SHADING_LANGUAGE_VERSION = ' + ctx5.getParameter(ctx5.SHADING_LANGUAGE_VERSION))
  // Vendor
  var Vendor = ctx5.getParameter(ctx5.VENDOR) === undefined ? '不支持该属性' : ctx5.getParameter(ctx5.VENDOR)
  resultWebgl.push(Vendor)
  console.log('VENDOR = ' + ctx5.getParameter(ctx5.VENDOR))
  // Renderer
  var Renderer = ctx5.getParameter(ctx5.RENDERER) === undefined ? '不支持该属性' : ctx5.getParameter(ctx5.RENDERER)
  resultWebgl.push(Renderer)
  console.log('RENDERER = ' + ctx5.getParameter(ctx5.RENDERER))
  // Antialias
  var bool_2_string = ctx5.getContextAttributes().antialias === undefined ? '不支持该属性' : ctx5.getContextAttributes().antialias
  resultWebgl.push(bool_2_string)
  console.log('antialias = ' + bool_2_string)
  // Angle
  var angle = ctx5.getParameter(ctx5.MAX_FRAGMENT_UNIFORM_VECTORS) === undefined ? 'True, Direct3D 11' : 'True, Direct3D 9'
  resultWebgl.push(angle)
  console.log('Angle = ' + angle)
  // Major Performance Caveat
  var caveat = ctx5.getContextAttributes().failIfMajorPerformanceCaveat === undefined ? '不支持该属性' : ctx5.getContextAttributes().failIfMajorPerformanceCaveat
  resultWebgl.push(caveat)
  console.log(ctx5.getContextAttributes().failIfMajorPerformanceCaveat)

  // Vertex Shader ：
  // Max Vertex Uniform Vectors
  var vectors = ctx5.getParameter(ctx5.MAX_VERTEX_UNIFORM_VECTORS) === undefined ? '不支持该属性' : ctx5.getParameter(ctx5.MAX_VERTEX_UNIFORM_VECTORS)
  resultWebgl.push(vectors)
  console.log(ctx5.getParameter(ctx5.MAX_VERTEX_UNIFORM_VECTORS))

  // Rasterizer :
  // ALIASED_LINE_WIDTH_RANGE
  function expandParamPair(pair_param) {
    return null == pair_param
      ? 'null'
      : '[' + pair_param[0] + ', ' + pair_param[1] + ']'
  }
  var ANGLE = expandParamPair(ctx5.getParameter(ctx5.ALIASED_LINE_WIDTH_RANGE)) === undefined ? '不支持该属性' : expandParamPair(ctx5.getParameter(ctx5.ALIASED_LINE_WIDTH_RANGE))
  resultWebgl.push(ANGLE)
  console.log('ANGLE = ' + ANGLE)

  // texture :
  // EXT_texture_filter_anisotropic :
  if(ctx5.getExtension('EXT_texture_filter_anisotropic')) {
    var anisotropic = ctx5.getExtension('EXT_texture_filter_anisotropic')
    var texture = ctx5.getParameter(anisotropic.MAX_TEXTURE_MAX_ANISOTROPY_EXT) === undefined ? '不支持该属性' : ctx5.getParameter(anisotropic.MAX_TEXTURE_MAX_ANISOTROPY_EXT)
    resultWebgl.push(texture)
  } else {
    resultWebgl.push('')
  }
  // var anisotropic = ctx5.getExtension('EXT_texture_filter_anisotropic')
  // var texture = ctx5.getParameter(anisotropic.MAX_TEXTURE_MAX_ANISOTROPY_EXT)
  // resultWebgl.push(texture)
  // console.log(ctx5.getParameter(anisotropic.MAX_TEXTURE_MAX_ANISOTROPY_EXT))

  // WEBGL_draw_buffers :
  draw_buffers_ext = ctx5.getExtension('WEBGL_draw_buffers')
  var WEBGL_draw_buffers = ctx5.getParameter(draw_buffers_ext.MAX_DRAW_BUFFERS_WEBGL) === undefined ? '不支持该属性' : ctx5.getParameter(draw_buffers_ext.MAX_DRAW_BUFFERS_WEBGL)
  resultWebgl.push(WEBGL_draw_buffers)
  console.log(ctx5.getParameter(draw_buffers_ext.MAX_DRAW_BUFFERS_WEBGL))

  var frag_prec_h_float = ctx5.getShaderPrecisionFormat(ctx5.FRAGMENT_SHADER, ctx5.HIGH_FLOAT)
  // resultWebgl.push(frag_prec_h_float)
  console.log(frag_prec_h_float)

  // Fragment Shader :
  // MAX_FRAGMENT_UNIFORM_VECTORS
  var shader = ctx5.getParameter(ctx5.MAX_FRAGMENT_UNIFORM_VECTORS) === undefined ? '不支持该属性' : ctx5.getParameter(ctx5.MAX_FRAGMENT_UNIFORM_VECTORS) 
  resultWebgl.push(shader)
  console.log('MAX_FRAGMENT_UNIFORM_VECTORS = ' + ctx5.getParameter(ctx5.MAX_FRAGMENT_UNIFORM_VECTORS))
  console.log(resultWebgl)
  return resultWebgl
}
