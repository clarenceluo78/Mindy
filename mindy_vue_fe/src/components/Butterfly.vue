<template>
  <div id="app">
    <butterfly-vue
      :canvasData="graphData"
    />
  </div>
</template>

<script>
import {ButterflyVue} from 'butterfly-vue';

import gridNode from './grid-node.vue';

export default {
  name: 'App',
  components: {
    ButterflyVue
  },
  data(){
    return{
      graphData: {
        groups: [],
        nodes: [
          {
            id: '0',
            left: 10,
            top: 10,
            label: '0',
            render: gridNode,
          }
        ],
        edges: [],
      },
    }
  },
}
</script>