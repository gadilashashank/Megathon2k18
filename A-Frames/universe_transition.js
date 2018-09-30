document.addEventListener('keydown', function(event) {
    console.log(event.keyCode)
    if(event.keyCode == 49) {
      document.getElementById('world1').setAttribute('visible','true')
      document.getElementById('world2').setAttribute('visible','false')
      document.getElementById('world3').setAttribute('visible','false')
    }
    
    else if(event.keyCode == 50 ) {
      document.getElementById('world1').setAttribute('visible','false')
      document.getElementById('world2').setAttribute('visible','true')
      document.getElementById('world3').setAttribute('visible','false')
    }
    
    else if(event.keyCode==51) {
      document.getElementById('world1').setAttribute('visible','false')
      document.getElementById('world2').setAttribute('visible','false')
      document.getElementById('world3').setAttribute('visible','true')
    }
});