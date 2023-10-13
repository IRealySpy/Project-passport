from flask import Flask, render_template
import requests

@app.route('/')
def hello_world():
    return f'''<link rel="stylesheet" type="text/css" href="https://nst1.gismeteo.ru/assets/flat-ui/legacy/css/informer.min.css">
<div id="gsInformerID-FtJV5I857Qf28m" class="gsInformer" style="width:240px;height:193px">
    <div class="gsIContent">
        <div id="cityLink">
            <a href="https://www.gismeteo.ru/weather-moscow-4368/" target="_blank" title="Погода в Москве">
                <img src="https://nst1.gismeteo.ru/assets/flat-ui/img/gisloader.svg" width="24" height="24" alt="Погода в Москве">
            </a>
            </div>
        <div class="gsLinks">
            <table>
                <tr>
                    <td>
                        <div class="leftCol">
                            <a href="https://www.gismeteo.ru/" target="_blank" title="Погода">
                                <img alt="Погода" src="https://nst1.gismeteo.ru/assets/flat-ui/img/logo-mini2.png" align="middle" border="0" width="11" height="16" />
                                <img src="https://nst1.gismeteo.ru/assets/flat-ui/img/informer/gismeteo.svg" border="0" align="middle" style="left: 5px; top:1px">
                            </a>
                            </div>
                            <div class="rightCol">
                                <a href="https://www.gismeteo.ru/weather-moscow-4368/2-weeks/" target="_blank" title="Погода в Москве на 2 недели">
                                    <img src="https://nst1.gismeteo.ru/assets/flat-ui/img/informer/forecast-2weeks.ru.svg" border="0" align="middle" style="top:auto" alt="Погода в Москве на 2 недели">
                                </a>
                            </div>
                        </td>
                </tr>
            </table>
        </div>
    </div>
</div>
<script async src="https://www.gismeteo.ru/api/informer/getinformer/?hash=FtJV5I857Qf28m"></script>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
