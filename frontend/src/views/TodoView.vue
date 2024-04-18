<script>
export default {
  // Properties returned from data() become reactive state
  // and will be exposed on `this`.
  data() {
    return {
      items: [],
      count: 0,
      selection: []
    }

  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    increment() {
      this.count++
    },
    delete(value){
      const index=this.items.indexOf(value[0])
      console.log(index,value)
      this.items.splice(index ,1)
    },
    add(value){
      this.items.push(value[0])

    },
    async get_list(){
      const response =  await fetch("http://${import.meta.env.VITE_IP}:5000/read",{
          method: "get",
          mode: "cors",
          cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
          credentials: "same-origin", // include, *same-origin, omit
          headers: {
             "Content-Type": "application/json",
              // 'Content-Type': 'application/x-www-form-urlencoded',
          },
          redirect: "follow",
          referrerPolicy: "no-referrer",
      })
      this.items = await response.json();
      this.items = this.items.msg
      console.log(this.items);
    }
  },

  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  mounted() {
    this.get_list()
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

<template>
  <div >
  <li v-for="(item,index) in items">
  <input type="checkbox" :id="index" :value="item" v-model="selection"/>
  <label :for="index">{{ item }}</label>
</li>
{{ selection }}

  <button @click="delete(selection)" >Delete </button>
  <button @click="add(selection)">Add </button>
</div>
</template>
