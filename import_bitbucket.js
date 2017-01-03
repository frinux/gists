var shell = require('shelljs'); //npm install -g shelljs

var arr = {
    "name": "bitbucket_name",
    "name2": "bitbucket_name2"
};

for (var url in arr) {
    var dest_name = arr[url];
    dest_name = encodeURIComponent(dest_name);
    var src_name = encodeURIComponent(url);

    var command = "curl 'https://bitbucket.org/repo/import' /* PUT HERE REAL CURL COMMAND SNIFFED FROM WEBDEVELOPPER TOOL */"

    shell.exec(command, function(code, output) {
        console.log('Exit code:', code);
        console.log('Program output:', output);
    });
}
