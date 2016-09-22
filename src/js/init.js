/**
 * Created by alex on 20.09.16.
 */
//getting selenium
var wd = require('selenium-webdriver');
var assert = require('assert');

//adding By method
By = wd.By;

//importing remote control for launching server
SeleniumServer = require('selenium-webdriver/remote').SeleniumServer;

//example url
var URL = 'https://www.netent.com/en/game/guns-and-roses/';

//init path to .jar file for standalone server
var pathToSeleniumJar = '../../selenium-server-standalone-2.44.0.jar';

//init port for launching standalone server
var server = new SeleniumServer(pathToSeleniumJar, {
    port: 4444
});
//starting server
server.start();
//setUP browser
var client = new wd.Builder()
    .usingServer(server.address())
    .withCapabilities({ browserName: 'chrome' })
    .build();

//testing func
client.get(URL).then(function() {
    client.findElement(By.className('logotype')).click();
    client.quit();
});
