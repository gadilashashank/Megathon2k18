  var view="SKY"
  var coods={x:1,y:1,z:1}

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
        document.getElementById('env').setAttribute('environment','preset:checkerboard')
      }
      
      else if(event.keyCode==51) {
        document.getElementById('world1').setAttribute('visible','false')
        document.getElementById('world2').setAttribute('visible','false')
        document.getElementById('world3').setAttribute('visible','true')
      }

      else if(event.keyCode==81) {
        if(view=="SKY")
        {
          document.getElementById('camera').setAttribute('position',document.getElementById('player').getAttribute('position'))
          view="First_Person"
        }
        else {
          view="SKY"
          document.getElementById('camera').setAttribute('position',"0 10 30")
        }
      }
      else if(event.keyCode==84) {
        var coods=document.getElementById('player').getAttribute('position')
        console.log(coods)
        var pos={x:0,y:0,z:0}
        pos.x=coods.x
        pos.y=coods.y
        pos.z=coods.z
        pos.z-=1
        document.getElementById('player').setAttribute('position',pos)
      }
      else if(event.keyCode==71) {
        var coods=document.getElementById('player').getAttribute('position')
        console.log(coods)
        var pos={x:0,y:0,z:0}
        pos.x=coods.x
        pos.y=coods.y
        pos.z=coods.z
        pos.z+=1
        document.getElementById('player').setAttribute('position',pos)
      }
      else if(event.keyCode==71) {
        var coods=document.getElementById('player').getAttribute('position')
        console.log(coods)
        var pos={x:0,y:0,z:0}
        pos.x=coods.x
        pos.y=coods.y
        pos.z=coods.z
        pos.x+=1
        document.getElementById('player').setAttribute('position',pos)
      }
  });