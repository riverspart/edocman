odoo.define('thmdocument.task_graph', function(require) {
"use strict";

    var Model = require('web.Model');

    var base = require('web_editor.base');
    var custom_model = new Model('thmdocument.task');



          base.ready().done(function() {

                $(document).on("click",'a[data-toggle="tab"]',function() {
                    var form = $('form.o_form_binary_form');
                    console.log(form);
                    var id_input = form.find('input[name=id]');
                    var fields = {};
                    fields.id = id_input.val();
                    custom_model.call('my_function',[fields]).then(function(result){
                          console.log(result);//show in console Hello
                        var data = JSON.parse(result);
                         var nodes = data[0].nodes;
                         var edges = data[0].edges;
                         var container = document.getElementById('mynetwork');
console.log(nodes);
                          if (container != null){
                               var data = {
                                    nodes: nodes,
                                    edges: edges
                                  };
                                  var options = {};
                                  var network = new vis.Network(container, data, options);
                          }
                    });

                    var nodes = [
                        {id: 1, label: 'Node 1'},
                        {id: 2, label: 'Node 2'},
                        {id: 3, label: 'Node 3'},
                        {id: 4, label: 'Node 4'},
                        {id: 5, label: 'Node 5'}
                    ];

                          // create an array with edges
                      var edges = [
                        {from: 1, to: 2, label: 'Node 4'},
                        {from: 1, to: 3},
                        {from: 2, to: 4},
                        {from: 2, to: 5}
                      ];
                     // create a network


                });

                // $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
                //     console.log(nodes);
                // })

               // console.log(nodes);//show in console Hello

          });

});
