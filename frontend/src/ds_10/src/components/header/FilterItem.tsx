import { motion } from "framer-motion"
import Popover from "../ui/Popover"
import { cn } from "../../lib/utils"
import { UrlState, urlState } from "bi-internal/core"
import { useSelector } from "react-redux"
import { useState } from "react"
import React from "react"
import { RootState } from "../../state/store"
import { filterItemDataType } from "./Filters"
import { Trash2 } from "lucide-react"
import SelectWithSearch from "../ui/SelectWithSearch"
import DatePicker from "../ui/DatePicker"

const FilterItem = ({ filterItemData }: { filterItemData: filterItemDataType }) => {

    const [open, setOpen] = useState(false)

    const urlModel = UrlState.getModel()
    const urlValue = urlModel[filterItemData.id]

    const activeSkillCategory: string | undefined = urlModel.knowledgeField

    const { knowledgeCategories, skillsByCategories, departments, employees } = useSelector((state: RootState) => state.filterOptions)

    const onItemClick = (value: string) => {

        if (filterItemData.id === 'knowledgeField') {
            urlState.updateModel({ knowledgeField: value, skill: undefined })
        }
        else {
            urlState.updateModel({ [filterItemData.id]: value })
        }
        setOpen(false)
    }

    return (
        <div className='h-full'>
            <Popover setOpen={setOpen}>
                <Popover.Trigger setOpen={setOpen}>
                    <li className={cn('flex gap-2 items-center px-4 py-3 h-full text-black hover:text-primary bg-white hover:bg-secondary cursor-pointer transition-all select-none', open && 'bg-secondary text-primary', urlValue && 'text-primary')}>
                        {filterItemData.icon}
                        <motion.h3
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ duration: 0.3, delay: 0.2, ease: 'easeIn' }}
                            key={urlValue}
                            className='text-lg'
                        >
                            {filterItemData.popoverContentType === 'DatePicker' ? (urlModel.halfyear === 'both' ? urlModel.year : `${urlModel.halfyear}-е полугодие ${urlModel.year}`) : urlValue || filterItemData.title}
                        </motion.h3>
                        {filterItemData.popoverContentType === 'DatePicker' && <Trash2 size={20} strokeWidth={1.5} className='text-rose-600' onClick={(e) => { e.stopPropagation(); urlState.updateModel({ year: '2024', halfyear: 'both' }) }} />}
                    </li>
                </Popover.Trigger>
                <Popover.Content open={open} align='center'>

                    {filterItemData.popoverContentType === 'SelectWithSearch' &&
                        <SelectWithSearch
                            options={filterItemData.id === 'knowledgeField' ? knowledgeCategories :
                                filterItemData.id === 'skill' && Object.keys(skillsByCategories).length > 0 && activeSkillCategory ? skillsByCategories[activeSkillCategory] :
                                    filterItemData.id === 'department' ? departments :
                                        filterItemData.id === 'employee' ? employees :
                                            filterItemData.options}
                            onClick={onItemClick}
                            onReset={() => {
                                if (filterItemData.id === 'knowledgeField') {
                                    urlState.updateModel({ knowledgeField: undefined, skill: undefined }, false)
                                }
                                else {
                                    urlState.updateModel({ [filterItemData.id]: undefined }, false)
                                }
                                setOpen(false);
                            }}
                            active={urlValue}
                        />
                    }

                    {filterItemData.popoverContentType === 'DatePicker' &&
                        <DatePicker setOpen={setOpen} />}

                </Popover.Content>
            </Popover>

        </div>
    )
}

export default FilterItem