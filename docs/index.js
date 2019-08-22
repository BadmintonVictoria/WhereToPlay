// Vue Grid Reference: https://vuejs.org/v2/examples/grid-component.html 
// Window Resize Reference:  https://codepen.io/sethdavis512/pen/EvNKWw

Vue.component('table-header', {
  template: '#grid-header'
})

Vue.component('table-grid', {
  template: '#grid-template',
  props: {
    json_list: Array
  }
})

var app = new Vue({
  el: '#app',
  data: {
    data_list: json_data,
    data_update: json_update
  }
})