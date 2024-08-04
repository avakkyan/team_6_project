import { BookOpenCheck, CalendarDays, CircleUserRound, ListCollapse, Network, Trash2 } from 'lucide-react'
import React from 'react'
import { urlState } from 'bi-internal/core'
import { motion } from 'framer-motion'
import FilterItem from './FilterItem'

export type filterItemDataType = filterSelectItemType | filterDateItemType

type filterSelectItemType = {
    id: string
    title: string
    icon: JSX.Element
    options: string[]
    popoverContentType: 'SelectWithSearch'
}

type filterDateItemType = {
    id: string,
    title: string
    icon: JSX.Element
    popoverContentType: 'DatePicker'
}

const filtersData: filterItemDataType[] = [
    {
        id: 'date',
        title: "Период",
        icon: <CalendarDays className='text-primary' size={20} strokeWidth={1.5} />,
        popoverContentType: 'DatePicker',
    },
    {
        id: 'knowledgeField',
        title: "Область знаний",
        icon: <ListCollapse className='text-primary' size={20} strokeWidth={1.5} />,
        options: [],
        popoverContentType: 'SelectWithSearch',
    },
    {
        id: 'skill',
        title: "Навык",
        icon: <BookOpenCheck className='text-primary' size={20} strokeWidth={1.5} />,
        options: [],
        popoverContentType: 'SelectWithSearch',
    },
    {
        id: 'department',
        title: "Подразделение",
        icon: <Network className='text-primary' size={20} strokeWidth={1.5} />,
        options: [],
        popoverContentType: 'SelectWithSearch'
    },
    {
        id: 'employee',
        title: "Сотрудник",
        icon: <CircleUserRound className='text-primary' size={20} strokeWidth={1.5} />,
        options: [],
        popoverContentType: 'SelectWithSearch',
    },

]

const Filters = () => {

    return (
        <>
            <motion.ul
                layout
                transition={{ duration: 0.3, ease: 'linear' }}
                className='flex divide-x border rounded w-fit'>
                {filtersData.map((filter) =>
                    <FilterItem filterItemData={filter} />
                )}
            </motion.ul>
            <div onClick={() => { urlState.updateModel({ year: '2024', halfyear: 'both', skill: undefined, employee: undefined, department: undefined, knowledgeField: undefined }) }} className='px-3 py-2 ml-2 bg-card border rounded hover:bg-rose-400 hover:text-white transition-all flex gap-2 items-center text-rose-400 cursor-pointer'>
                <Trash2 />
            </div>
        </>
    )
}

export default Filters