<script lang="ts">
import {
    defineComponent, computed
} from '@vue/composition-api';
import { cities, highlightCity } from '../store';
import { City } from '../types';


export default defineComponent({
    setup() {
        const sortedCities = computed(
            () => cities.value.sort((a: City, b: City) => a.name.localeCompare(b.name))
        )
        return {
            cities,
            sortedCities,
            highlightCity,
        }
    }
})
</script>

<template>
    <v-navigation-drawer
        right
        absolute
        permanent
    >
        <v-card color="transparent">
            <v-card-title>Results ({{ cities.length }})</v-card-title>
            <v-container>
                <v-row
                    v-for="city in sortedCities"
                    :key="city.id"
                    @click="() => highlightCity(city.id)"
                >
                    <v-col>{{ city.name }}</v-col>
                </v-row>
            </v-container>
        </v-card>
    </v-navigation-drawer>
</template>
