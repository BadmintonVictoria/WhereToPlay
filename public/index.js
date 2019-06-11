// Vue Grid Reference: https://vuejs.org/v2/examples/grid-component.html 
// Window Resize Reference:  https://codepen.io/sethdavis512/pen/EvNKWw

Vue.component('table-grid', {
  template: '#grid-template',
  props: {
    json_list: Array,
    columns: Array,
    filterKey: String
  },
  data: function () {
    var sortOrders = {}
    this.columns.forEach(function (key) {
      sortOrders[key] = 1
    })
    return {
      sortKey: '',
      sortOrders: sortOrders
    }
  },
  computed: {
    filtered_json_list: function () {
      var sortKey = this.sortKey
      var filterKey = this.filterKey && this.filterKey.toLowerCase()
      var order = this.sortOrders[sortKey] || 1
      var json_list = this.json_list
      if (filterKey) {
        json_list = json_list.filter(function (row) {
          return Object.keys(row).some(function (key) {
            return String(row[key]).toLowerCase().indexOf(filterKey) > -1
          })
        })
      }
      if (sortKey) {
        json_list = json_list.slice().sort(function (a, b) {
          a = a[sortKey]
          b = b[sortKey]
          return (a === b ? 0 : a > b ? 1 : -1) * order
        })
      }
      return json_list
    }
  },
  filters: {
    capitalize: function (str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    }
  },
  methods: {
    sortBy: function (key) {
      this.sortKey = key
      this.sortOrders[key] = this.sortOrders[key] * -1
    }
  }
})

// bootstrap the demo
var app = new Vue({
  el: '#app',
  data: {
    searchQuery: '',
    gridColumns: ['DayOfWeek', 'GroupDescription',  'TimeRange' ],
    gridData: json_data,
    lastUpdate: json_update,
    window: {
      width: 0,
      height: 0
    }
  },
  created() {
    window.addEventListener('resize', this.handleResize)
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
      if (this.window.width>1200) {
        this.gridColumns = ['DayOfWeek', 'GroupDescription', 'GeneralArea', 'Location', 'PlayerLevel', 'PlayerAge', 'Shuttle', 'TimeRange', 'Season' ];
      } else {
        if (this.window.width>1000) {
          this.gridColumns = ['DayOfWeek', 'GroupDescription', 'Location', 'PlayerLevel', 'Shuttle', 'TimeRange', 'Season' ];
        } else {
          if (this.window.width>800) {
            this.gridColumns = ['DayOfWeek', 'GroupDescription', 'Location', 'PlayerAge', 'TimeRange' ];
          } else {
            this.gridColumns = ['DayOfWeek', 'GroupDescription',  'TimeRange' ];
          }
        }
      }

    }
  }
})