#include "lists.h"

/**
 * insert_node - inserts a node
 *
 * @head: the pointer to the head of the linked list
 * @number: the number to include in the n node field
 * Return: pointer to the new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (head && *head)
	{
		listint_t *new;
		listint_t *tmp;
		listint_t *tmp2;

		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);

		new->n = number;
		tmp = *head;
		if (number < 0)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		while (tmp->next != NULL)
		{
			if (tmp->n > number)
			{
				tmp2->next = new;
				new->next = tmp;
				return (new);
			}
			tmp2 = tmp;
			tmp = tmp->next;
		}
		if (tmp->next == NULL)
		{
			tmp->next = new;
			new->next = NULL;
		}
		return (NULL);
	}
	return (NULL);
}
