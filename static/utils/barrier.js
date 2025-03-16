
function Barrier(f) {
  this.f = f;

  this.registered = 0;
  this.outstanding = {"size":0};
}

Barrier.prototype.run = function() {
  if(this.outstanding.size == 0) {
    this.f();
  }
}

// 返回一个标签。传递此标签以通知您何时准备就绪。
Barrier.prototype.register = function(tag) {
  if(tag !== undefined) {
    if(! (tag in this.outstanding)) {
      // 如果你重新注册一个标签，语义会有点模糊。（不要这样）
      this.outstanding[tag] = true;
      this.outstanding.size++;
    }
    return;
  }

  var i = this.registered;
  this.registered++;

  this.outstanding[i] = true;
  this.outstanding.size++;
  return i;
}

Barrier.prototype.notify = function(tag) {
  var debug = 1;

  if(tag in this.outstanding) {
    delete(this.outstanding[tag]);
    this.outstanding.size--;
  }

  this.run();
}

