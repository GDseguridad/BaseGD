window.setInterval(
    function ()
    {
        var d = new Date();
        var hour = d.getHours() + ':' + d.getMinutes()
        let hoursActive = ['15:22']
        if (hoursActive.includes(hour) <= hour)
        {
            document.getElementById('btn').style.display = 'block';
        }
        else
        {
            document.getElementById('btn').style.display = 'none';
        }
    }
    , 2000);