<script setup>
import VFragment from '@/components/VFragment.vue';
import SettingControls from './SettingControls.vue';
import { SettingsItem } from '@/SettingsItem.js';
import { computed } from 'vue';
import { useTextTooltipStore } from '@/stores/textTooltipStore.js';

const tip = useTextTooltipStore();
const model = defineModel();
const props = defineProps(['item']);

const types = SettingsItem.types;

const colSize = computed(() => `col${props.item.colSize !== undefined ? props.item.colSize == '' ? '' : '-' + props.item.colSize 
                                                        : props.item.type == types.column ? '-auto' : ''}`);

const classObj = computed(() => {
    let obj =  { 'pb-2': !props.item.children.length || props.item.children[0].type != types.color };

    if (props.item.padding) {
        obj[props.item.padding] = true;
    }

    return obj;
});
</script>

<template>
    <template v-if="item.visibleCondition() && (!item.settingName || item.settingBind)">
        <component :is="item.includeRow ? 'div' : VFragment" class="row" :class="classObj">
            <component :is="item.includeCol ? 'div' : VFragment" :class="colSize" @mouseenter="tip.tooltip(item.type == types.color ? '' : item.tooltip, $event)">
                <component :is="item.type == types.group ? 'fieldset' : VFragment" class="form-group">
                    <SettingControls v-model="model" :item="item" />

                    <template v-for="child in item.children" :key="child">
                        <SettingsBlock v-model="child.settingBind" :item="child" />
                    </template>
                </component>
            </component>
        </component>
    </template>
</template>

<style scoped>
</style>