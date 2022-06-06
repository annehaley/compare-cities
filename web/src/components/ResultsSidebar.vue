<script lang="ts">
import {
    defineComponent
} from '@vue/composition-api';
import { cities, highlightCity } from '../store';


export default defineComponent({
    setup() {
        return {
            cities,
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
                    v-for="city in cities"
                    :key="city.id"
                    @click="() => highlightCity(city.id)"
                >
                    <v-col>{{ city.name }}</v-col>
                </v-row>
            </v-container>
        </v-card>
    </v-navigation-drawer>
</template>
