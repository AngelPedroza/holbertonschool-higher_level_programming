#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if the linked list is a cycle.
 * @list: Address of each node
 * Return: 1 cycle, 0 no cycle.
 */
int check_cycle(listint_t *list)
{
	if (list)
	{
		listint_t *tmp;
		int i;

		tmp = list;
		for (i = 0; list != NULL; i++)
		{
			list = list->next;
			if (tmp < list)
			{
				i++;
				return (1);
			}
			tmp = tmp->next;
		}
		return (0);
	}
	return (0);
}
