//WebGL fingerprinting
function webglDemo() {
  try {
    var fa2s = function(fa) {
        gl.clearColor(0.0, 0.0, 0.0, 1.0);
        gl.enable(gl.DEPTH_TEST);
        gl.depthFunc(gl.LEQUAL);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        return "[" + fa[0] + ", " + fa[1] + "]";
    };
    var maxAnisotropy = function(gl) {
        var anisotropy, ext = gl.getExtension("EXT_texture_filter_anisotropic") || gl.getExtension("WEBKIT_EXT_texture_filter_anisotropic") || gl.getExtension("MOZ_EXT_texture_filter_anisotropic");
        return ext ? (anisotropy = gl.getParameter(ext.MAX_TEXTURE_MAX_ANISOTROPY_EXT), 0 === anisotropy && (anisotropy = 2), anisotropy) : null;
    };
    var canvas = document.getElementById("webglRep");
    var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    var result = [];
    var vShaderTemplate = "attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}";
    var fShaderTemplate = "precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}";
    var vertexPosBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexPosBuffer);
    var vertices = new Float32Array([-.2, -.9, 0, .4, -.26, 0, 0, .732134444, 0]);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
    vertexPosBuffer.itemSize = 3;
    vertexPosBuffer.numItems = 3;
    var program = gl.createProgram(), vshader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vshader, vShaderTemplate);
    gl.compileShader(vshader);
    var fshader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fshader, fShaderTemplate);
    gl.compileShader(fshader);
    gl.attachShader(program, vshader);
    gl.attachShader(program, fshader);
    gl.linkProgram(program);
    gl.useProgram(program);
    program.vertexPosAttrib = gl.getAttribLocation(program, "attrVertex");
    program.offsetUniform = gl.getUniformLocation(program, "uniformOffset");
    gl.enableVertexAttribArray(program.vertexPosArray);
    gl.vertexAttribPointer(program.vertexPosAttrib, vertexPosBuffer.itemSize, gl.FLOAT, !1, 0, 0);
    gl.uniform2f(program.offsetUniform, 1, 1);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, vertexPosBuffer.numItems);
    if (gl.canvas != null) { result.push(gl.canvas.toDataURL()); }
    result.push("extensions:" + gl.getSupportedExtensions().join(";"));
    result.push(fa2s(gl.getParameter(gl.ALIASED_LINE_WIDTH_RANGE)));
    result.push(fa2s(gl.getParameter(gl.ALIASED_POINT_SIZE_RANGE)));
    result.push(gl.getParameter(gl.ALPHA_BITS));
    result.push((gl.getContextAttributes().antialias ? "yes" : "no"));
    result.push(gl.getParameter(gl.BLUE_BITS));
    result.push(gl.getParameter(gl.DEPTH_BITS));
    result.push(gl.getParameter(gl.GREEN_BITS));
    result.push(maxAnisotropy(gl));
    result.push(gl.getParameter(gl.MAX_COMBINED_TEXTURE_IMAGE_UNITS));
    result.push(gl.getParameter(gl.MAX_CUBE_MAP_TEXTURE_SIZE));
    result.push(gl.getParameter(gl.MAX_FRAGMENT_UNIFORM_VECTORS));
    result.push(gl.getParameter(gl.MAX_RENDERBUFFER_SIZE));
    result.push(gl.getParameter(gl.MAX_TEXTURE_IMAGE_UNITS));
    result.push(gl.getParameter(gl.MAX_TEXTURE_SIZE));
    result.push(gl.getParameter(gl.MAX_VARYING_VECTORS));
    result.push(gl.getParameter(gl.MAX_VERTEX_ATTRIBS));
    result.push(gl.getParameter(gl.MAX_VERTEX_TEXTURE_IMAGE_UNITS));
    result.push(gl.getParameter(gl.MAX_VERTEX_UNIFORM_VECTORS));
    result.push(fa2s(gl.getParameter(gl.MAX_VIEWPORT_DIMS)));
    result.push(gl.getParameter(gl.RED_BITS));
    result.push(gl.getParameter(gl.RENDERER));
    result.push(gl.getParameter(gl.SHADING_LANGUAGE_VERSION));
    result.push(gl.getParameter(gl.STENCIL_BITS));
    result.push(gl.getParameter(gl.VENDOR));
    result.push(gl.getParameter(gl.VERSION));
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.HIGH_FLOAT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.HIGH_FLOAT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.HIGH_FLOAT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_FLOAT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_FLOAT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_FLOAT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.LOW_FLOAT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.LOW_FLOAT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.LOW_FLOAT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_FLOAT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_FLOAT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_FLOAT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.MEDIUM_FLOAT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.MEDIUM_FLOAT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.MEDIUM_FLOAT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.LOW_FLOAT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.LOW_FLOAT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.LOW_FLOAT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.HIGH_INT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.HIGH_INT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.HIGH_INT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_INT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_INT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_INT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.LOW_INT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.LOW_INT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.LOW_INT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_INT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_INT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_INT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.MEDIUM_INT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.MEDIUM_INT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.MEDIUM_INT ).rangeMax);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.LOW_INT ).precision);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.LOW_INT ).rangeMin);
    result.push(gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.LOW_INT ).rangeMax);
    webGLData = result.join("ยง");
    console.log('webglResult' + result)
    console.log('webGLData' + webGLData)
  
    canvas = document.getElementById('webglRep');
    var ctx = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    if(ctx.getSupportedExtensions().indexOf("WEBGL_debug_renderer_info") >= 0) {
        webGLVendor = ctx.getParameter(ctx.getExtension('WEBGL_debug_renderer_info').UNMASKED_VENDOR_WEBGL);
        webGLRenderer = ctx.getParameter(ctx.getExtension('WEBGL_debug_renderer_info').UNMASKED_RENDERER_WEBGL);
    } else {
        webGLVendor = "Not supported";
        webGLRenderer = "Not supported";
    }
  } catch(e){
    webGLData = "Not supported";
    webGLVendor = "Not supported";
    webGLRenderer = "Not supported";
  }
  return result;
} 

