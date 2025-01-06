<!--
  File: frontend/src/components/PasswordOptions.vue
  Purpose: Component for password generation options (length, case, symbols, numbers)
-->
<template>
  <div class="space-y-4">
    <div class="flex items-center justify-between">
      <label class="text-gray-700">Length: {{ options.length }}</label>
      <input
        type="range"
        v-model.number="localOptions.length"
        min="10"
        max="20"
        class="w-1/2 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
      />
    </div>

    <div class="space-y-2">
      <div class="flex items-center space-x-2">
        <input
          type="checkbox"
          v-model="localOptions.useUppercase"
          class="rounded text-blue-500 focus:ring-blue-500"
        />
        <label class="text-gray-700">Include Uppercase</label>
      </div>

      <div class="flex items-center space-x-2">
        <input
          type="checkbox"
          v-model="localOptions.useSymbols"
          class="rounded text-blue-500 focus:ring-blue-500"
        />
        <label class="text-gray-700">Include Symbols</label>
      </div>

      <div class="flex items-center space-x-2">
        <input
          type="checkbox"
          v-model="localOptions.useNumbers"
          class="rounded text-blue-500 focus:ring-blue-500"
        />
        <label class="text-gray-700">Include Numbers</label>
      </div>
    </div>

    <button
      @click="generatePassword"
      class="w-full px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
    >
      Generate Password
    </button>
  </div>
</template>

<script>
export default {
  name: 'PasswordOptions',
  props: {
    options: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      localOptions: { ...this.options }
    }
  },
  watch: {
    localOptions: {
      handler(newValue) {
        this.$emit('update:options', newValue)
      },
      deep: true
    }
  },
  methods: {
    generatePassword() {
      this.$emit('generate')
    }
  }
}
</script>
