<script lang="ts">
import {
  defineComponent,
} from '@vue/composition-api';

export default defineComponent({
  setup() {
    return {};
  },
});
</script>

<template>
  <div
    ref="map"
    class="map"
  />
</template>

<style scoped>
.map {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  overflow: hidden;
}
</style>
